class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}"
