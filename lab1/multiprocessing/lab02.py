import requests
import multiprocessing
import re


session = None

def get_session():
    global session
    if not session:
        requests.Session()


def check_proxy(proxy):
    session = get_session()
    try:
        session.get('https://omgtu.ru', proxies={"https": "https://" + proxy}, timeout=5)
    except Exception as x:
        print('Proxy: ' + proxy + ' doesnt work' )
        return False
    return True


def collect_proxy(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
        
    return thread_check_proxy(proxys_list)
        


def thread_check_proxy(proxy_list):
    with multiprocessing.Pool(initializer=get_session) as pool:
        res = pool.map(abc, proxy_list)
        return list(res)
    
def abc(proxy):
    if check_proxy(proxy):
        return proxy
    