class InvalidEmailException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


def email_validation(value: str):
    if '@' and '.' in value:
        return value
    else:
        raise InvalidEmailException('email must contain @ and .')


def password_validation(value):
    if len(value) > 4:
        return value
    else:
        raise InvalidPasswordException('password must be more than four characters')
