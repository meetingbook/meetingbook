from domain.value_objects.password import Password
import bcrypt


class WorkWithPassword(Password):

    def prepare_psw_for_db(self):
        hashed_psw = bcrypt.hashpw(self.get_password().encode(), bcrypt.gensalt()).decode()
        return hashed_psw
