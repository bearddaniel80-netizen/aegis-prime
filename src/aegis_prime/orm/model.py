from .query import Query

# -----------------------------
# MODEL SYSTEM
# -----------------------------

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name != "Model":
            new_cls._model_name = name
        return new_cls


class Model():
    __where__: dict = {}
    __fields__ = None

    @classmethod
    def query(cls):
        q = Query(cls)

        if cls.__fields__:
            q = q.select(*cls.__fields__)

        if cls.__where__:
            q = q.where(**cls.__where__)

        return q

    @classmethod
    def where(cls, **conds):
        return cls.query().where(**conds)
