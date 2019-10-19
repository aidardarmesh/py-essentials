import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.storage = {}
    
    def process_data(self, payload):
        command, data = payload.split(' ', 1)
        data = data.strip()

        if command == 'put':
            metric, value, timestamp = data.split()

            self.storage[metric] = ' '.join([value, timestamp])

            return 'ok\n\n'
        elif command == 'get':
            res = 'ok\n'

            if data == '*':
                for key in self.storage:
                    res += ' '.join(key, self.storage[key]) + '\n'
            elif data in self.storage:
                res += ' '.join(key, self.storage[key]) + '\n'
            
            res += '\n'

            return res
        else:
            return 'error\nwrong command\n\n'

    def data_received(self, data):
        resp = self.process_data(data.decode())
        # self.process_data(data.decode())
        self.transport.write(resp.encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8181
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()