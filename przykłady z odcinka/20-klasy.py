# User
# Name
# Mail
# Age

class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.mail)
        print(self.age)

    def is_male(self):
        return self.name[-1:] != 'a'



user1 = User('Michal', 'flakpack29@gmail.com ', 19)

user = User('Adam', 'szy67@gmail.com', 27)


user1.print_info()
user.print_info()
if user.is_male() == True:
    print("chłop")
else:
    print("baba")
# print(user.name)
# print(user1.age)