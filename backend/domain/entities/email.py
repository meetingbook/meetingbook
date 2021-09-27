class InvalidEmailException(Exception):
    pass


class Email:
    def __init__(self, value: str):
        if '@' and '.' in value:
            self._email = value
        else:
            raise InvalidEmailException(f'email ({value}) must contain @ and .')

    def get_value(self):
        return self._email


if __name__ == '__main__':
    print(Email("asd.@").get_mail())
