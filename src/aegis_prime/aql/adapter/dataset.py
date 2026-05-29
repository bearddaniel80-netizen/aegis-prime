class Dataset:
    def __init__(self, rows, model_cls):
        self.rows = rows
        self.model_cls = model_cls

    def as_rows(self):
        return self.rows

    def schema(self):
        return self.model_cls