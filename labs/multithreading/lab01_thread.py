import requests
from concurrent.futures import ThreadPoolExecutor, thread
import re

from requests.sessions import session


def get_session():
    return requests.Session()


def check_proxy(proxy):
    session = get_session()
    with session:
        try:
            r = session.get('https://www.google.ru', proxies={"https": "https://" + proxy}, timeout=5)
            if r.status_code == requests.codes.ok:
                return True
        except Exception as x:
            print('Proxy: ' + proxy + ' doesnt work' )
            return False
        


def collect_proxy(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return thread_check_proxy(proxys_list)
        


def thread_check_proxy(proxy_list):
    with ThreadPoolExecutor(max_workers=300) as thread:
        res = thread.map(call_check_proxy, proxy_list)
        return list(res)
    
def call_check_proxy(proxy):
    if check_proxy(proxy):
        return proxy

        