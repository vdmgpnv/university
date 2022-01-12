import requests
import re
import asyncio
import aiohttp


# функция принимает url и объект-стратегию, которая парсит прокси с этого url
def collect_proxy(url, strategic):
    return strategic(url)

# функция собирает прокси и вызывает проверку, работает ли прокси для url
def collect_proxy_from_git(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return proxys_list


def collect_proxy_from_2ip(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return proxys_list

# функция проверяет работу прокси
async def check_proxy(proxy, tm):
    async with aiohttp.ClientSession() as session:
        try:
            session.get('https://www.google.ru',
                        proxies={"https": "https://" + proxy}, timeout=tm)
        except Exception as x:
            print('Proxy: ' + proxy + ' doesnt work')
            return False
        return True


async def call_check_proxy(proxy, tm):
    if check_proxy(proxy, tm):
        return proxy

async def async_check_proxy(proxy_list, tm=3):
    tasks = []
    for proxy in proxy_list:
        task = asyncio.ensure_future(call_check_proxy(proxy, tm))
        tasks.append(task)
    res = await asyncio.gather(*tasks, return_exceptions=True)
    return res
