class Message:
    def __init__(self, data):
        self.id = data.get("id")
        self.content = data.get("content")
        self.author = data.get("author")

    def __str__(self):
        return f"Message({self.id}): {self.content}"

class User:
    def __init__(self, data):
        self.id = data.get("id")
        self.username = data.get("username")

    def __str__(self):
        return f"[!] User({self.id}): {self.username}"