import sys
from crawl.session import NaverSession
from bs4 import BeautifulSoup
from crawl.article import NaverCafeArticleMetaData
from crawl.article import FootsalMatchingArticle
from crawl.NotLoginError import NotLoginError


class NaverCrawler:

    def __init__(self):
        self.session=NaverSession()
        self.is_logined=False

    def login(self, user_id, user_pwd):
        """
            Try Naver Login
        :return: None
        """
        result = self.session.login(user_id, user_pwd)

        if result is True:
            self.is_logined = True

        return result

    def logout(self):
        pass

    def gather_latest_matching_article(self):
        menu_id_list = [464,465,466,467,468,469]

        if self.is_logined is False:
            raise NotLoginError()

        for menu_id in menu_id_list:
            url ='http://cafe.naver.com/ArticleList.nhn?search.clubid=11367414&search.menuid={menu_id}&search.boardtype=L'.format(menu_id=menu_id)
            data = self.session.create_http_get(url)
            article_list = list()
            article_list.append(NaverCafeArticleMetaData(title="==========={category}===========".format(category=menu_id)))
            if data.status_code == 200:
                raw_data = BeautifulSoup(data.text, 'html.parser')
                article_list.extend(self.__parse_footsal_article(raw_data))

        return article_list

    def __parse_footsal_article(self, raw_data):
        """
            Translate html article list to python 'list'

        :param raw_data: 
        :return: article_list
        :rtype: list
        """

        article_list = list()
        articles = raw_data.find("div", {"class": "article-board m-tcol-c"}).find('form', {'name': 'ArticleList'}).findAll('tr', {'align': 'center'})
        category_name = raw_data.find('div', {'id': 'sub-tit'}).get_text()

        for raw_article in articles:
            article_id = raw_article.find('span', {'class': 'list-count'}).get_text()
            title = raw_article.find('a').get_text()
            url = raw_article.find('a')['href']

            # read view counts, written_time, likes
            view_counts = raw_article.findAll('td', {'class': 'view-count m-tcol-c'})
            written_time = view_counts[0].get_text().replace("\r\n", "").replace(" ", "")
            hits = view_counts[1].get_text()
            likes = view_counts[2].find('em').get_text()

            article = NaverCafeArticleMetaData(
                article_id=article_id,
                title=title,
                url=url,
                written_time=written_time,
                hits=hits,
                likes=likes,
                category=category_name)

            article_list.append(article)

            # print(str(article))

        return article_list

if __name__=='__main__':
    pass

