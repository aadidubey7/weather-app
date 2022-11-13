from models.user import UserModel

class UserController:
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def register(self):
        usermodel_obj = UserModel(
                self.username,
                self.email,
                self.password
            )
        usermodel_obj.save()
        return True
    
    @classmethod
    def login(cls, attempted_email, attempted_password):
        user = UserModel.find_by_email(attempted_email)
        if user and user.check_password_match(attempted_password):
            return user