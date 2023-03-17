from aiohttp import ClientSession
from lxml.html import fromstring
from .headers import get_headers
from .extract_data import *
from .errors import MissingToken
from .xpaths import XPATHS

async def get_token(session):
        """Get dmrFormToken"""
        async with session.get("https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej", headers=get_headers(), allow_redirects=True) as resp:
            content = await resp.text()
        source = fromstring(content)
        try:
            token = source.xpath(XPATHS["other"]["token"])[0].get("value")
            url = source.xpath(XPATHS["other"]["token_url"])[0].get("action")
            return token, url
        except (TypeError, KeyError):
            raise MissingToken("The scraper wasn't able to get a token from motorregister.skat.dk, the site may have changed.")

async def scrape_async(license_plate:str):

    async with ClientSession() as session:
        # Get dmrFormToken required to make site requests and get url to post data
        token, new_url = await get_token(session)

        payload = {
            "dmrFormToken": token,
            "soegeord": license_plate,
            "soegekriterie:": "REGISTRERINGSNUMMER",
            new_url: "Søg"
        }

        async with session.post('https://motorregister.skat.dk' + new_url, data=payload, headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url}), allow_redirects=True) as resp:
            content = await resp.text()

        if "Ingen køretøjer fundet." in content:
            # license plate doesn't exist
            return None

        # Page 1 scrape
        source = fromstring(content)
        data = page_1(source)

        new_url_without_last_16_chars = new_url[:-16]

        # Page 2 scrape
        async with session.get(str(resp.url) + "&_eventId=customPage&_pageIndex=1", headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url_without_last_16_chars}), allow_redirects=True) as resp:
            content = await resp.text()
        source = fromstring(content)
        data.update(page_2(source))

        # Page 4 scrape
        async with session.get(str(resp.url) + "&_eventId=customPage&_pageIndex=3", headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url_without_last_16_chars}), allow_redirects=True) as resp:
            content = await resp.text()
        source = fromstring(content)
        data.update(page_4(source))

    return data