from requests import Session
from lxml.html import fromstring
from typing import Optional
from .headers import get_headers
from .extract_data import page_1, page_2, page_4, get_token_and_url


def get_token(session) -> tuple[str, str]:
    """Get dmrFormToken"""
    resp = session.get("https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej", headers=get_headers(), allow_redirects=True)
    source = fromstring(resp.text)
    token, url = get_token_and_url(source)
    return token, url


def scrape(license_plate: str) -> Optional[dict]:

    with Session() as session:
        # Get dmrFormToken required to make site requests and get url to post data
        token, new_url = get_token(session)

        payload = {
            "dmrFormToken": token,
            "soegeord": license_plate,
            "soegekriterie:": "REGISTRERINGSNUMMER",
            new_url: "Søg"
        }

        resp = session.post('https://motorregister.skat.dk' + new_url, data=payload, headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url}), allow_redirects=True)

        if "Ingen køretøjer fundet." in resp.text:
            # license plate doesn't exist
            return None

        # Page 1 scrape
        source = fromstring(resp.text)
        data = page_1(source)

        # Page 2 scrape
        resp = session.get(str(resp.url) + "&_eventId=customPage&_pageIndex=1", headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url[:-16]}), allow_redirects=True)
        source = fromstring(resp.text)
        data.update(page_2(source))
        
        # Page 4 scrape
        resp = session.get(str(resp.url) + "&_eventId=customPage&_pageIndex=3", headers=get_headers({"Referer":"https://motorregister.skat.dk" + new_url[:-16]}), allow_redirects=True)
        if "Ingen forsikring" not in resp.text:
            source = fromstring(resp.text)
            data.update(page_4(source))
        else:
            data.update({"insurance": None})

    return data
