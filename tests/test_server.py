import unittest

from lsp.LanguageServer import LanguageServer

class TestServer(unittest.TestCase):
    def test_server_start_tcp(self):
        server = LanguageServer()

        server.start_tcp("127.0.0.1", 5000)

if __name__ == '__main__':
    unittest.main()
