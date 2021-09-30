import unittest
import time

from labs.multiprocessing.lab02_refac import collect_proxy, multi_proc_check_proxy

#@unittest.skip
class Testlab02(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()


    def test_collect_proxy(self):
        self.site = 'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt'          
        res = collect_proxy(self.site)
        self.assertTrue(len(res) != 0)
        valid_proxies = multi_proc_check_proxy(res)
        print(list(filter(lambda x : x is not None, valid_proxies)))



    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
