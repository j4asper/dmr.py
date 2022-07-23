from requests import Session
from lxml.html import fromstring
from .headers import get_headers
from .clean_data import clean
from .extract_data import *

def scrape(licens_plate):
    def get_token(session):
        """Get dmrFormToken"""
        resp = session.get("https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej", headers=get_headers(), allow_redirects=True)
        source = fromstring(resp.text)
        try:
            token = source.xpath('/html/body/div[2]/div/div[1]/div[2]/form/input')[0].get("value")
            url = source.xpath('/html/body/div[2]/div/div[1]/div[2]/form')[0].get("action")
            return token, url
        except (TypeError, KeyError):
            raise Exception("The scraper wasn't able to get a token from motorregister.skat.dk, the site may have changed.")

    with Session() as session:
        # Get dmrFormToken required to make site requests and get url to post data
        token, new_url = get_token(session)

        payload = {
            "dmrFormToken": token,
            "soegeord": licens_plate,
            "soegekriterie:": "REGISTRERINGSNUMMER",
            new_url: "Søg"
        }

        resp = session.post('https://motorregister.skat.dk' + new_url, data=payload, headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url}), allow_redirects=True)

        if "Ingen køretøjer fundet." in resp.text:
            # Licens plate doesn't exist
            return None

        source = fromstring(resp.text)
        data = page_1(source)

        second_page = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[1]/ul/li[2]/div/a')[0].get("href")

        resp = session.get("https://motorregister.skat.dk" + second_page, headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url[:-16]}), allow_redirects=True)

        source = fromstring(resp.text)
        data.update(page_2(source))

    return clean(data)