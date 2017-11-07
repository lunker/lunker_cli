import unittest
import sys

sys.path.insert(0, "/Users/voiceloco/work/pythonspace/lunker_cli/src/crawl")
import crawler

class TestCrawl(unittest.TestCase):
    '''
    @brief test case using uniitest.TestCase
    '''

    def setUp(self):
        self.crawler=crawler.NaverCrawler()
        pass

    def tearDown(self):
        ''' @brief this method is called after every test methods '''
        pass

    def test_login(self):
        # user_id = ''
        # user_pwd = ''
        result = self.crawler.login(user_id, user_pwd)

        self.assertTrue(result)

    def test_gather_naver(self):
        # user_id = ''
        # user_pwd = ''
        url = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=11367414&search.menuid=464&search.boardtype=L'

        result_login = self.crawler.login(user_id, user_pwd)

        self.assertTrue(result_login)

        self.crawler.gather_latest_matching_article(url)


if __name__ == '__main__':
    '''
    test_main() 과 같이 테스트 하는 대신
    unittest.main() 으로 호출하여 테스트를 진행하면 전체 OK, Not OK 여부가 나오고
    아래와 같이 두줄을 표시해 주면 상단의 test001_init ... ok, test002_doA ... ok 와 같이 출력됨.
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCrawl)
    unittest.TextTestRunner(verbosity=2).run(suite)

