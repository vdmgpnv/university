import unittest
import time

from lab1.multiprocessing.lab02 import collect_proxy


class Testlab02(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()


    def test_collect_proxy(self):
        self.site = 'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt'          
        res = collect_proxy(self.site)
        


    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
