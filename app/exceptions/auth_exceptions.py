class EmailNotFoundError(Exception):
    pass

class PasswordInvalidError(Exception):
    pass

class EmailNotVerifiedError(Exception):
    pass

class AccessDeniedError(Exception):
    pass

class TokenExpiredError(Exception):
    pass
