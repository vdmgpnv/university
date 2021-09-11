import unittest
import time

from lab1.multithreading.lab01 import collect_proxy

@unittest.skip
class Testlab01(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()


    def test_collect_proxy(self):
        self.site = 'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt'          
        res = collect_proxy(self.site)


    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')
