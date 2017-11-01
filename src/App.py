import cli.app

@cli.app.CommandLineApp
def ls(app):
    print ("run -l")
    print (app)
    print (app.name)
    pass

ls.add_param("-l", "--long", help="list in long format", default=False, action="store_true")
ls.add_param("-k", "--kong", help="list in long format", default=False, action="store_true")

'''
class LunkerCli(cli.app.CommandLineApp):
    def main(self):
        print("in main")

LunkerCli.add_param("-l", "--long", help="list in long format", default=False, action="store_true")
'''

class LunkerCli:
    @staticmethod
    def run():
        print ("Enter commands: ")
        while True==True :
            data=input()
            print (data)
            break
    

if __name__ == "__main__":
    #ls.run()
    LunkerCli.run()


