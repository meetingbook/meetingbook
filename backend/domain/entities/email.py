class InvalidEmailException(Exception):
    pass


class Email:
    def __init__(self, value: str, *args):
        if '@' and '.' in value:
            self._email = value
        else:
            raise InvalidEmailException(f'email ({value}) must contain @ and .')
        super().__init__(*args)

    def get_mail(self):
        return self._email


if __name__ == '__main__':
    print(Email("asd.@").get_mail())
