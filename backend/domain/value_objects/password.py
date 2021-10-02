import bcrypt


class InvalidPasswordException(Exception):
    pass


class Password:
    def __init__(self, password):
        if len(password) > 4:
            self._password = password
        else:
            raise InvalidPasswordException('password must be more than four characters')

    def get_value(self):
        return self._password

    def get_hashed_password(self):
        hashed_psw = bcrypt.hashpw(self._password.encode(), bcrypt.gensalt()).decode()
        return hashed_psw
