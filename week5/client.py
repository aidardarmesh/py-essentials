import socket

class ClientError(Exception):
    pass

class Client:
    """
    Клиент для работы с сервером метрик
    """

    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or str(int(time.time()))

        with socket.create_connection((self.ip, self.port), self.timeout) as s:
            s.send("put {} {} {}\n".format(metric, value, timestamp).encode('utf-8'))

    def get(self, metric):
        answer = ''

        with socket.create_connection((self.ip, self.port), self.timeout) as s:
            s.send("get {}\n".format(metric).encode('utf-8'))
            answer = s.recv(1024)

        res = {}
        answer = answer.decode(encoding='utf-8')
        lines = list(filter(lambda x: x, answer.split('\n')))

        if lines[0] == "ok":
            del lines[0]
        else:
            raise ClientError
        
        for line in lines:
            metric, value, timestamp = tuple(line.split())

            if metric in res:
                res[metric].append((int(timestamp), float(value)))
            else:
                res[metric] = [(int(timestamp), float(value))]

            res[metric].sort()
        
        return res