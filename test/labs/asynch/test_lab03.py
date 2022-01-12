import unittest
import time
import asyncio

from labs.asynch.lab03 import async_check_proxy, collect_proxy, collect_proxy_from_git, async_check_proxy

#@unittest.skip
class Testlab01(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()

    def test_collect_proxy(self):
        self.site = 'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt'
        res = collect_proxy(self.site, collect_proxy_from_git)
        self.assertTrue(len(res) != 0)
        valid_proxies = asyncio.get_event_loop().run_until_complete(async_check_proxy(res))
        print(list(filter(lambda x: x is not None, valid_proxies)))

    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
