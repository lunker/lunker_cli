import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger("Client__")


class Client:
    def __init__(self, name, nickname, comp):
        self.name = name
        self.comp = comp
        self.nickname = nickname

    def create_client(self, name, nickname, comp):
        logger.debug("Create Client")
        return Client(name, nickname, comp)

    def register_client (self):
        pass

    def print_client(self):
        client_info_template = "[Client] "
        client_info_template += "name: {0}\t"
        client_info_template += "nickname: {1}\t"
        client_info_template += "comp: {2}\t"

        logger.debug(client_info_template.format(self.name, self.nickname, self.comp))

    def print_room_list(self):
        """
            Print current chatting room list in chat server
            
        :return: Room List 
        """
        pass

if __name__ == '__main__':
    print("main")
      
