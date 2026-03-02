# 1

class BankAccount:

    def __init__(self):

        self.__balance = 0

    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:

            self.__balance -= amount

    @property

    def balance(self):

        return self.__balance

account = BankAccount()

account.deposit(100)

account.withdraw(40)

print(account.balance)

# 2

class UserProfile:

    def __init__(self):

        self.__email = ""

    @property

    def email(self):

        return self.__email

    @email.setter

    def email(self, value):

        if "@" in value:

            self.__email = value

user = UserProfile()

user.email = "test@example.com"

print(user.email)

# 3

class Battery:

    def __init__(self):

        self.__charge = 100

    @property

    def charge(self):

        return self.__charge

    @charge.setter

    def charge(self, value):

        if 0 <= value <= 100:

            self.__charge = value

battery = Battery()

battery.charge = 80

print(battery.charge)

# 4

class Speaker:

    def __init__(self):

        self.__volume = 5

    @property

    def volume(self):

        return self.__volume

    @volume.setter

    def volume(self, value):

        if 0 <= value <= 10:

            self.__volume = value

speaker = Speaker()

speaker.volume = 7

print(speaker.volume)

# 5

class Character:

    def __init__(self):

        self.__health = 100

    def damage(self, amount):

        self.__health = max(0, self.__health - amount)

    def heal(self, amount):

        self.__health = min(100, self.__health + amount)

    @property

    def health(self):

        return self.__health

hero = Character()

hero.damage(30)

hero.heal(10)

print(hero.health)

# 6

class PasswordManager:

    def __init__(self, password):

        self.__password = password

    def change_password(self, old, new):

        if old == self.__password and len(new) >= 8:

            self.__password = new

            return True

        return False

manager = PasswordManager("oldpass123")

print(manager.change_password("oldpass123", "newpassword456"))
