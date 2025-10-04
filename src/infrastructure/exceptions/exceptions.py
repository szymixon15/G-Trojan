class SessionNoneError(Exception):
    def __init__(self):
        super().__init__("Error: SQL Alchemy repository needs a Session object")