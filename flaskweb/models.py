from flaskweb import db, login_manager

# Method to return the user object
# Accept the user's email
@login_manager.user_loader
def load_user(email):
    userjson = db.user.find_one({'email': email})
    if not userjson:
        return None
    return User(email=userjson['email'], username=userjson['username'])

# Define a class for user
class User:
    def __init__(self, email, username):
        self.email = email
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.email

