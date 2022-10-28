class Profile:
    def __init__(self,username,password):
        self.username = username
        self.password = password



    @property
    def username(self):

        return self.__username
    
    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        length = len(value) >= 8
        upper = any([True for x in value if x.isupper()])
        digit = any([True for x in value if x.isdigit()])

        if length and upper and digit:
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'




correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

