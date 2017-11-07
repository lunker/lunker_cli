class NotLoginError(Exception):
    def __str__(self):
        return "Need to login before execute"
