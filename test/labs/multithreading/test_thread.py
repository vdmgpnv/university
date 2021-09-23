import unittest
import time

from labs.multithreading.thread import check_sites


@unittest.skip
class TestSync(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()


    def test_set_sites(self):
        self.sites = ['https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt', 
                      'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt',
                      'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt',
                      'https://github.com/opsxcq/proxy-list/blob/master/list.txt',
                      'https://github.com/x-o-r-r-o/proxy-list/blob/master/proxy-list.txt']*25

        res = check_sites(self.sites)
        self.assertEqual(len(self.sites), len(res))


    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f"{self.id()}: Downloaded {len(self.sites)} in {duration} seconds")
        print('-------------------------------------------------------------')
        
