import unittest
from client import client

class TestApp(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        ''' @brief this method is called before every test methods '''
        pass
    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass
    def test001_init(self):
        clientA=client()
        #self.assertTrue(my.a == 'a' and my.b == 'b')

if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApp)
    unittest.TextTestRunner(verbosity=2).run(suite)

