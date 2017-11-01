import unittest
import xlrd

import sys
sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/excel")

import parser

class TestParser(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''
    def setUp(self):
        self.par=parser.Parser('/Users/voiceloco/Downloads/jejuPublic.xlsx')
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    '''
        노선분류에 따라 해당 버스노선 정보가 담겨있는 엑셀을 불러온다.
    '''
    def load_route_map(self):
        pass

    '''
        엑셀에서 원하는 버스의 시트 index를 불러온다 
    '''
    def find_sheet_index(self):
        bus_num='701-1'
        sheet_index=self.par.find_sheet_index_by_bus_num(bus_num)

        # Get valid sheet index 
        self.assertNotEqual(sheet_index, -1)
        pass

    def test_print_bus_time_table(self):
        bus_num = '701-1'
        sheet_index = self.par.find_sheet_index_by_bus_num(bus_num)

        self.par.print_bus_time_table(sheet_index)
        pass

if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
    unittest.TextTestRunner(verbosity=2).run(suite)


