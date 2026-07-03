class OrderBy:
    def __init__(self, field, descending=False):
        self.field = field
        self.descending = descending

    def __repr__(self):
        return (
            f"OrderBy({self.field}, "
            f"desc={self.descending})"
        )