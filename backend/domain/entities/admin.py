from domain.entities.email import Email
from domain.value_objects.password import Password


class Admin(Email, Password):
    def __init__(self, email, password, admin_id=-1):
        super().__init__(email, password)
        self.__id = admin_id

    def get_id(self):
        return self.__id


# a = Admin('mail@.', 'hvj@.hkj')
# print(a.get_mail(), a.get_password(), a.get_id())
