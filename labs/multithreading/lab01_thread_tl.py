import time
import requests
from concurrent.futures import ThreadPoolExecutor, thread
import re
import threading

from requests.sessions import session

thread_local = threading.local()

def long_session_init():
    time.sleep(1)
    return requests.Session()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = long_session_init()
    return thread_local.session


def check_proxy(proxy):
    session = get_session()
    with session:
        try:
            session.get('https://www.google.ru', proxies={"https": "https://" + proxy}, timeout=5)
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

        