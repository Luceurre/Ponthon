import asyncio
import logging
from lsp.LanguageServerProtocol import LanguageServerProtocol

class Server:
    """A generic server class."""

    def __init__(self, protocol_cls):
        super().__init__()

        self.protocol = protocol_cls()
        self.loop = asyncio.get_event_loop()

    def start_tcp(self, host, port):
        print(f"Starting TCP server on {host}:{port}")

        self._server = self.loop.run_until_complete(
            self.loop.create_server(self.protocol, host=host, port=port)
            )

        try:
            self.loop.run_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            self.shutdown()

    def start_io(self, stdin, stdout):
        logging.info(f"Starting IO server")

    def shutdown(self):
        logging.info(f"Server shutdown")

class LanguageServer(Server):
    """Handle communication with the client."""

    def __init__(self):
        super().__init__(LanguageServerProtocol)
