class Admin:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self.id = None

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_id(self):
        return self.id
