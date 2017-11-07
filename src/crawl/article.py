import datetime


class NaverCafeArticleMetaData:

    def __init__(self,
                 article_id="-1",
                 title="None",
                 written_time="00:00",
                 url="https:google.com",
                 hits=0,
                 likes=0,
                 category="None",
                 content="Comming Soon ..."):

        self.article_id = article_id
        self.title = title
        self.written_time = written_time
        self.url = "http://cafe.naver.com" + url
        self.hits = hits
        self.likes = likes
        self.category = category
        self.content = content
        pass

    '''
    def __init__(self):
        pass
    

    # article_id
    @property
    def article_id(self):
        return self.article_id

    def article_id(self, article_id):
        self.article_id = article_id

    # article_title
    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def written_time(self):
        return self.written_time

    @written_time.setter
    def written_time(self, written_time):
        self.written_time = written_time

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, url):
        self.url = url

    @property
    def hits(self):
        return self.hits

    @hits.setter
    def hits(self, hits):
        self.hits=hits

    @property
    def likes(self):
        return self.likes

    @likes.setter
    def likes(self, likes):
        self.likes = likes
    '''

    def __str__(self):
        article_to_str = "Naver Cafe Article::\n"
        article_to_str += "Id: {article_id}\n"
        article_to_str += "Title: {title}\n"
        article_to_str += "Url: {url}\n"
        article_to_str += "Written Time: {written_time}\n"
        article_to_str += "Hits: {hits}\n"
        article_to_str += "Likes: {likes}\n"
        article_to_str += "Content: {content}\n"

        return article_to_str.format(
            article_id=self.article_id,
            title=self.title, url=self.url, written_time=self.written_time,
            hits=self.hits, likes=self.likes,

            category=self.category, content=self.content)


class FootsalMatchingArticle(NaverCafeArticleMetaData):
    def __init__(self):
        pass

