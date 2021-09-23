from concurrent.futures import ThreadPoolExecutor
import requests



def get_session():
    return requests.Session()


def download_site(url):
    session = get_session()
    with session:
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")
            return f"Read {len(response.content)} from {url}"



def check_sites(sites):
    with ThreadPoolExecutor(max_workers=20) as thread:
        res = thread.map(download_site, sites)
        return list(res)
