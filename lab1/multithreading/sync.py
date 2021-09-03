import requests
from requests.sessions import session


def download_site(url, session):
    with session.get(url) as res:
        #print(f'Read {len(res.content)} from {url}')
        return f'Read {len(res.content)} from {url}'

def check_sites(sites):
    res = []
    with requests.Session() as session:
        for url in sites:
            res.append(download_site(url, session))
    return res
