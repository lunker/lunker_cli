import socket 

class Server(object):
    instance=None
    is_run=True

    def __init__(self):
        self.url = None
        self.port = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        self.server_address = ('localhost', 10000)
        self.sock.bind(self.server_address)
        self.fd_list = None

    @staticmethod
    def getInstance(self):
        if Server.instance is None:
            self.instance="!!!"
            Server.instance=Server()
        return Server.instance

    def handle_request(self):
        pass

    def run(self):

        # Listen 
        self.sock.listen(1)

        while self.is_run:
            connection, client_address=self.sock.accept()


if __name__ == '__main__':
    Server.main()
    print("run server")
