import asyncio


class ClientServerProtocol(asyncio.Protocol):
    storage = {}

    def connection_made(self, transport):
        self.transport = transport
    
    def process_data(self, payload):
        if len(payload.split()) < 2:
            return 'error\nwrong command\n\n'
        
        command, data = payload.split(' ', 1)
        data = data.strip()

        if command == 'put':
            metric, value, timestamp = data.split()

            if not metric in type(self).storage:
                type(self).storage[metric] = []
            
            for t, v in type(self).storage[metric]:
                if timestamp == t:
                    return 'ok\n\n'

            type(self).storage[metric].append((timestamp, value))

            return 'ok\n\n'
        elif command == 'get':
            res = 'ok\n'

            if data == '*':
                for key in type(self).storage:
                    type(self).storage[key].sort()

                    for timestamp, value in type(self).storage[key]:
                        res += ' '.join([key, value, timestamp]) + '\n'
            elif data in type(self).storage:
                for timestamp, value in type(self).storage[data]:
                    res += ' '.join([data, value, timestamp]) + '\n'
            
            res += '\n'

            return res
        else:
            return 'error\nwrong command\n\n'

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':
    run_server('127.0.0.1', 8888)