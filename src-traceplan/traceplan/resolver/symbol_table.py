from .models import Symbol

class SymbolTable:

    def __init__(self):

        self._symbols = {}

    def register(
        self,
        symbol: Symbol
    ):

        self._symbols[
            symbol.fqdn
        ] = symbol

    def resolve(
        self,
        name: str
    ):

        for symbol in self._symbols.values():

            if symbol.name == name:
                return symbol

        return None