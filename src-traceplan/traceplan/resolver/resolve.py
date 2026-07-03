class Resolver:

    def __init__(
        self,
        symbol_table
    ):
        self.symbol_table = symbol_table

    def resolve(
        self,
        name
    ):

        symbol = (
            self.symbol_table.resolve(
                name
            )
        )

        if not symbol:
            return None

        return symbol.fqdn