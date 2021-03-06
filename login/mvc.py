## The success return code
SUCCESS               =   1
## Cannot find the user/password pair in the database (for login only)
ERR_BAD_CREDENTIALS   =  -1
## invalid user name (empty or longer than MAX_USERNAME_LENGTH) (for login or add)
ERR_BAD_USERNAME      =  -3
## invalid password name (longer than MAX_PASSWORD_LENGTH) (for add)
ERR_BAD_PASSWORD      =  -4
## trying to add a user that already exists (for add only)
ERR_USER_EXISTS       =  -2
## The maximum length of user name
MAX_USERNAME_LENGTH = 128
## The maximum length of the passwords
MAX_PASSWORD_LENGTH = 128

def login(self, user, password):
    """ This function checks the user/password in the database.
    * On success, the function updates the count of logins in the database.
    * On success the result is either the number of logins (including this one) (>= 1)
    * On failure the result is an error code (< 0) from the list below
    * ERR_BAD_CREDENTIALS"""
    if user not in self.users:
        return UsersModel.ERR_BAD_CREDENTIALS

    data = self.users[user]
    if data.password != password:
        return UsersModel.ERR_BAD_CREDENTIALS
    data.count += 1
    return data.count


def add(self, user, password):
    """This function checks that the user does not exists, the user name is not empty.
    * On success the function adds a row to the DB, with the count initialized to 1
    * On success the result is the count of logins
    * On failure the result is an error code (<0) from the list below
    * ERR_BAD_USERNAME, ERR_BAD_PASSWORD, ERR_USER_EXISTS"""
    if user in self.users:
        return UsersModel.ERR_USER_EXISTS
    def valid_username(username):
        return username != "" and len(username) <= UsersModel.MAX_USERNAME_LENGTH

    def valid_password(password):
        return len(password) <= UsersModel.MAX_PASSWORD_LENGTH
        
    if not valid_username(user):
        return UsersModel.ERR_BAD_USERNAME
    if not valid_password(password):
        return UsersModel.ERR_BAD_PASSWORD
        
    self.users[user] = UserData(user, password)
    assert self.users[user].count == 1
    return self.users[user].count
    

