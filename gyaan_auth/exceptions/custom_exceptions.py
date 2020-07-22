class InvalidUsername(Exception):
    pass


class InvalidPassword(Exception):
    pass


class InvalidUserID(Exception):
    pass


class InvalidUserIds(Exception):
    def __init__(self, invalid_user_ids):
        self.invalid_user_ids = invalid_user_ids
