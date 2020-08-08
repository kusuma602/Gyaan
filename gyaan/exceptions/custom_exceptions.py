class InvalidDomainID(Exception):
    pass


class InvalidPostIds(Exception):
    def __init__(self, invalid_post_ids):
        self.invalid_post_ids = invalid_post_ids


class UserNotDomainMember(Exception):
    pass

