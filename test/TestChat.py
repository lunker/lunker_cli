import unittest
import sys
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/chat/client")
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/chat/server")

import client
import server

class TestChat(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        self.psy=client.Client("park", "psy", "theKids")
        self.lunker=client.Client("lee", "lunker", "voiceloco")

        # Create Server
        # self.server=server.Server.getInstance()
        # self.server.run()
        
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    def test_create_room(self):
        pass
        
    def test_print_room_list(self):
        self.psy.print_room_list()
        pass

if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChat)
    unittest.TextTestRunner(verbosity=2).run(suite)

