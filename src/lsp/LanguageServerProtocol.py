from jsonrpc.JsonObject import export
import asyncio
import logging as logger

class LanguageServerProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()

        self.headers = {
            "Content-Length": 0,
            "Content-Type": ""
        }

        self.content = None

    def generate_headers(self):
        headers = ""

        for header_name in self.headers.keys():
            header_value = self.headers[header_name]

            headers += f"{header_name}: {header_value}" + "\n\r"

        return headers

    def generate_content(self):
        content = export(self.content)

        return content

    def generate_message(self):
        return self.generate_headers() + "\n\r" + self.generate_message()


    def connection_made(self, transport):
        super().connection_made(transport)

        print("Connection made.")
        self.transport = transport

    def data_received(self, data):
        super().data_received(data)

        print('Received {!r}'.format(data))

    def __call__(self):
        """Needed to accept TCP connection."""
        return self
