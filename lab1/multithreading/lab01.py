import requests
import re


def check_proxy(proxy):
    with requests.Session() as session:
        try:
            session.get('https://www.google.ru', proxies={"https": "https://" + proxy}, timeout=5)
        except Exception as x:
            print('Proxy: ' + proxy + ' doesnt work' )
            return False
        return True
    
    

def collect_proxy(url):
    valid_proxies = []
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    for proxy in proxys_list:
        if check_proxy(proxy):
            valid_proxies.append(proxy)
    print(valid_proxies)
    


