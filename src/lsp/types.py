from jsonrpc.JsonObject import json_object, json_field, validate_json_field
from jsonrpc.JsonRPCObject import JsonRPCObject
from jsonrpc.JsonRPCRequestObject import JsonRPCRequestObject
from jsonrpc.JsonRPCResponseObject import JsonRPCResponseObject
from jsonrpc.JsonRPCErrorObject import JsonRPCErrorObject

class BaseStructure:
    pass

Message = JsonRPCObject
RequestMessage = JsonRPCRequestObject
ResponseMessage = JsonRPCResponseObject
ResponseError = JsonRPCErrorObject

EOL = ['\n', '\r\n', '\r']
ENCODING = "UTF-16"

@json_object
class CancelParams:
    def __init__(self, request_to_cancel_id):
        self.cancel_id = request_to_cancel_id

    @json_field("id")
    def get_cancel_id(self):
        return self.cancel_id

    @staticmethod
    @validate_json_field("id")
    def validate_cancel_id(cancel_id):
        try:
            int(cancel_id)
        except TypeError:
            raise TypeError("id should be a string or an int")

@json_object
class Position:
    """Position in a UTF-16 text document expressed as zero based line/character offset."""
    def __init__(self, line, character):
        super().__init__()
        self.line = line
        self.character = character

    @json_field("line")
    def get_line(self):
        return self.line

    @json_field("character")
    def get_character(self):
        return self.character

@json_object
class Range:
    def __init__(self, start, end):
        super().__init__()

        self.start = start
        self.end = end

    @json_field("start")
    def get_start(self):
        return self.start

    @json_field("end")
    def get_end(self):
        return self.end

@json_object
class Location:
    def __init__(self, uri, selection: Range):
        super().__init__()

        self.selection = selection
        self.uri = uri

    @json_field("range")
    def get_range(self):
        return self.selection

    @json_field("uri")
    def get_uri(self):
        return self.uri

@json_object
class Command:
    def __init__(self, title, command, arguments=None):
        super().__init__()

        self.title = title
        self.command = command
        self.arguments = arguments

    @json_field("title")
    def get_title(self):
        return self.title

    @json_field("command")
    def get_command(self):
        return self.command

    @json_field("arguments")
    def get_arguments(self):
        return self.arguments


@json_object
class TextEdit:
    def __init__(self, selection: Range, newText):
        super().__init__()

        self.selection = selection
        self.newText = newText

    @json_field("range")
    def get_range(self):
        return self.selection

    @json_field("newText")
    def get_newText(self):
        return self.newText

@json_object
class TextDocumentEdit:
    def __init__(self, textDocument, edits):
        super().__init__()

        self.textDocument = textDocument
        self.edits = edits

    @json_field("textDocument")
    def get_textDocument(self):
        return self.textDocument

    @json_field("edits")
    def get_edits(self):
        return self.edits


@json_object
class WorkDoneProgressParams:
    def __init__(self, workDoneToken=None):
        super().__init__()

        self.workDoneToken = workDoneToken

    @json_field("workDoneToken")
    def get_workDoneToken(self):
        return self.workDoneToken

@json_object
class InitializeParams(WorkDoneProgressParams):
    def __init__(self, capabilities, processId=None, clientInfo=None, locale=None, rootPath=None, rootUri=None, initializationOptions=None, workDoneToken=None, trace=None, workspaceFolders=None):
        super().__init__(workDoneToken=workDoneToken)


@json_object
class ClientCapabilities:
    def __init__(self, workspace=None, textDocument=None, window=None, general=None, experimental=None):
        super().__init__()

@json_object
class InitializeResult:
    def __init__(self, capabilities, serverInfo=None):
        super().__init__()

@json_object
class ServerCapabilities:
    def __init__(self, textDocumentSync=None, completionProvider=None, signatureHelpProvider=None,
                 declarationProvider=None, hoverProvider=None, definitionProvider=None, typeDefinitionProvider=None, implementationProvider=None, referencesProvider=None,
                 documentHighlightProvider=None, documentSymbolProvider=None, codeActionProvider=None, codeLensProvider=None, documentLinkProvider=None, colorProvider=None,
                 documentFormattingProvider=None, documentRangeFormattingProvider=None):
        super().__init__()
