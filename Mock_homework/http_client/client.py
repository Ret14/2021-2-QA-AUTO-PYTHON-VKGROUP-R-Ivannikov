import socket


class HttpClient:

    def __init__(self, host='127.0.0.1', port='5000'):
        self.host = host
        self.port = port

    def resp_data(self, client):
        total_data = []
        data = client.recv(4096)

        while data:
            total_data.append(data.decode())
            data = client.recv(4096)

        client.close()
        return ''.join(total_data).splitlines()

    def get(self, params='/'):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((self.host, int(self.port)))
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        client.send(request.encode())
        return self.resp_data(client)

    def post(self, params='/', data=None):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # init TCP socket type
        client.connect((self.host, int(self.port)))
        request = f"POST {params} HTTP/1.1\r\nHost: {self.host}\r\nContent-Type:"\
                  f" application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n {data}"
        client.send(request.encode())  # send DATA to server'
        return self.resp_data(client)

    def put(self, params='/', data=None):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # init TCP socket type
        client.connect((self.host, int(self.port)))
        request = f"POST {params} HTTP/1.1\r\nHost: {self.host}\r\nContent-Type:" \
                  f" application/json\r\nContent-Length: {len(data)}\r\n\r\n {data}"
        client.send(request.encode())  # send DATA to server'
        return self.resp_data(client)

    def put_request(self, params='/', data=None):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # init TCP socket type
        client.connect((self.host, int(self.port)))
        request = f"PUT {params} HTTP/1.1\r\nHost: {self.host}\r\nContent-Type:"\
                  f" application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n {data}"
        client.send(request.encode())  # send DATA to server'
        return self.resp_data(client)

    def delete(self, params='/'):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((self.host, int(self.port)))
        request = f'DELETE {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        client.send(request.encode())
        return self.resp_data(client)
