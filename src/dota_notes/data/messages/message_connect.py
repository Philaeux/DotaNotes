class MessageConnect:
    """Ask the client to connect with specific credentials

    Attributes:
        user: steam username
        password: steam password
    """
    user: str
    password: str

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password


class MessageDisconnect:
    pass
