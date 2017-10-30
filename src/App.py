import cli.app

@cli.app.CommandLineApp
class LunkerCli(cli.app.CommandLineApp):
	def main(self):
		print ("in main")
		print(self)
	def handle_l(self):
		print ("handle l")

#LunkerCli.add_param("-l", "--long",  default=False, action="store_true", help="list in long format")
LunkerCli.add_param("-l", "--long",  default=False, action="store_true", help="list in long format")

if __name__ == "__main__":
    LunkerCli.run()



