import unittest
import sys
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/util")

import logger

class TestLogger(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''

    def setUp(self):
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    def test_logging(self):
        self.logger = logger.LoggerFactory.get_logger(self.__class__.__name__)

        self.logger.debug("hi!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogger)
    unittest.TextTestRunner(verbosity=2).run(suite)

