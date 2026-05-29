class BaseHandler:
    def can_handle(self, ast) -> bool:
        raise NotImplementedError

    def handle(self, ast):
        raise NotImplementedError