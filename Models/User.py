# user entity definition

class User():
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.age = None
        self.email = None
        self.password_hash = None
        self.password_salt = None
        self.profile_url = None # Bonus, as noted in the documents