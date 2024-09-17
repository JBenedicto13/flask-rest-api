class ReturnFormat:
    def __init__(self, data=None, message=""):
        self.data = data
        self.message = message

    def to_dict(self):
        return {"data": self.data, "message": self.message}