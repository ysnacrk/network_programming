import socket , errno , os
from threading import Thread


"""
-------WEB SERVER ARCHITECTURE-------
-Server create socket and listen given port
-Client create socket and connect the server's port (our browser doing for us)
-Server get connection request and create thread , get the message by recv function and parsing with split function
-Server create a http response and send then close connection because client can waiting response forever 


"""
class WebServer:


    def __init__(self):

        self.server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            
    
    def create_thread(self, connection , adress):
        resp_message = ""
        try:
            while True:

                recv_message = connection.recv(2048).decode()
                header = recv_message.split("\n")
                first_list = header[0].split()

                if first_list[0] == "GET":

                    if first_list[1]== "/":
                        resp_message = "HTTP/1.1 200 OK\n"
                        resp_message += "Content-Type: text/html ; charset=utf-8\n"
                        resp_message += "\n"
                        resp_message += "<html><body>Server on fire !!!</body> </html>\n"

                    else:
                        path = first_list[1]
                        list_dir = os.listdir()
                        print(list_dir)
                        temp = str(path[1:]) + ".html"

                        if temp in list_dir:
                            f = open(str(path[1:]) + ".html" , "r")
                            resp_message = "HTTP/1.1 200 OK\n"
                            resp_message += "Content-Type: text/html ; charset=utf-8\n"
                            resp_message += "\n"
                            resp_message += f.read()
                        
                        else:
                            resp_message = "HTTP/1.1 404 Not Found\n"
                            resp_message += "Content-Type: text/html ; charset=utf-8\n"
                            resp_message += "\n"
                            resp_message += "<html><body>Sayfa bulunamadı</body> </html>\n"
                        
                connection.sendall(resp_message.encode())
                connection.shutdown(socket.SHUT_WR) 

        except IOError as e:
            print(e)

    def run_server(self ,ip_adress , port):
        self.server.bind((ip_adress , port))
        self.server.listen(5)

        while True:
            
            connection , adress = self.server.accept()
            
            print("{} bağlandı " .format(adress))

            thread = Thread(target=self.create_thread , args=(connection , adress))
            thread.start()

        self.server.close()    
            

if __name__ == '__main__':
    server = WebServer()
    server.run_server('localhost' , 8001)
