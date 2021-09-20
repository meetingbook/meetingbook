class InvalidPasswordException(Exception):
    pass


class Password:
    def __init__(self, password, *args):
        if len(password) > 4:
            self.__password = password
        else:
            raise InvalidPasswordException('password must be more than four characters')
        super().__init__(*args)

    def get_password(self):
        return self.__password


