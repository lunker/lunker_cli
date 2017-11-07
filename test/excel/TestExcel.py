import unittest
import xlrd

import sys
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/excel")

import parser, loader
import os



class TestExcel(unittest.TestCase):

    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        self.loader = loader.Loader()
        self.parser = parser.Parser("asdf")
        print(self.parser.create_bus_timetable.__doc__)
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    def test_load_excel_files(self):

        for file_name in self.loader.search('/Users/voiceloco/bus_timetable'):
            print("from generator")
            self.parser.create_bus_timetable(file_name)

        pass

if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExcel)
    unittest.TextTestRunner(verbosity=2).run(suite)