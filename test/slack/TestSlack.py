import unittest
import sys
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/util")

import slack

class TestSlack(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    def test_send_message(self):
        slack_bot = slack.SlackHelper()
        slack_bot.send_message("a")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSlack)
    unittest.TextTestRunner(verbosity=2).run(suite)

