import unittest
import time

from labs.multithreading.lab01_thread import collect_proxy

@unittest.skip
class Testlab01(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()


    def test_collect_proxy(self):
        self.site = 'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt'          
        res = collect_proxy(self.site)
        #result = list(filter(lambda x : x is not None, res))
        print(res)


    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
