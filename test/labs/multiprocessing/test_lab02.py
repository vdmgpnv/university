import unittest
import time

from labs.multiprocessing.lab02 import collect_proxy

@unittest.skip
class Testlab02(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()


    def test_collect_proxy(self):
        self.site = 'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt'          
        res = collect_proxy(self.site)
        result = list(filter(lambda x : x is not None, res))
        print(result)



    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
