
class Message:
    def __init__(self, type_url: str, value: bytes):
        self.type_url = type_url
        self.value = value
