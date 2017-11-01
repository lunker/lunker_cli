import socket 

class Server(object):
    __instance=None
    __is_run=True

    def __init__(self):
        self.url=None
        self.port=None
        self.sock=socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
        self.server_address=('localhost', 10000)
        self.sock.bind(self.server_address)

        pass

    @staticmethod
    def getInstance(self):
        if __instance is None:
            __instance=Server()
        return __instance

    def handle_request(self):
        pass

    def run(self):

        # Listen 
        self.sock.listen(1)

        while __is_run:
            connection, client_address=sock.accept()

            data=connection.
            
        pass

if __name__ == '__main__':
    Server.main()
    print("run server")
