import cli.app
from crawl.crawler import NaverCrawler
from futsal.futsal import FutsalFinder

@cli.app.CommandLineApp
def LunkerCli(app):
    """
    print("run -l")
    print(app)
    print(app.name)
    print(app.params)
    """

    if app.params.match is True:
        app.futsal_finder = FutsalFinder()
        app.futsal_finder.search_latest_matching()


LunkerCli.add_param("-m", "--match", help="find futsal matching articles", default=False, action="store_true")

if __name__ == "__main__":
    try:
        LunkerCli.run()
    except Exception as ex:
        print("올바른 명령어를 입력해라 ")
        print(ex)

