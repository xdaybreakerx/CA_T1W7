class UserAccount():
    def __init__(self, email, password, username) -> None:
        self._email = email
        self._password = password
        self._username = username
        
    def getEmail(self):
        return self._email

    def setEmail(self, newEmail):
        self._email = newEmail

    def getUsername(self): 
        return self._username
    
    def setUsername(self, newUsername):
        self._username = newUsername
        
    def getPassword(self):
        return self._password

    def setPassword(self, newPassword):
        if len(newPassword) < 5:
            print("Password does not meet requirements")
        else:
            self._password = newPassword


newUser = UserAccount("test@email.com", "Password1", "testUser")

print(newUser.getUsername())
newUser.setUsername("RandomUser")
print(newUser.getUsername())

print(newUser.getEmail())
newUser.setEmail("newEmail@email.com")
print(newUser.getEmail())

print(newUser.getPassword())
newUser.setPassword("newPassword")
print(newUser.getPassword())
newUser.setPassword("error")