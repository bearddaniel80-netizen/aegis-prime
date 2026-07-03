class GroupBy:
    def __init__(self, fields):
        self.fields = fields

    def __repr__(self):
        return f"GroupBy( fields = {', '.join(self.fields)} )"

    def to_dict(self):
        return {
            "type": "GroupBy",
            "fields": ', '.join(self.fields)
        }