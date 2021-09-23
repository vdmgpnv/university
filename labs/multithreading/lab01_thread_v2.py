import requests
from concurrent.futures import ThreadPoolExecutor, thread
import re
import urllib.request

def check_proxy(proxy):
        try:
            urllib.request.urlopen('https://www.google.ru', proxies={"https": "https://" + proxy}, timeout=15)
        except Exception as x:
            print('Proxy: ' + proxy + ' doesnt work' )
            return False
        return True


def collect_proxy(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return thread_check_proxy(proxys_list)
        


def thread_check_proxy(proxy_list):
    with ThreadPoolExecutor(max_workers=300) as thread:
        res = list(thread.map(call_check_proxy, proxy_list))
        return res
    
def call_check_proxy(proxy):
    if check_proxy(proxy):
        return proxy

        