from hashlib import md5
from country_code_checker import getCountryCode


class User:
    def __init__(self, username, password, fname='', lname='', country='iran', phonenumber=''):
        self.__fname = ''
        self.__lname = ''
        self.__country_code = ''
        self.__phonenumber = ''
        self.__username = ''
        self.__password = ''

        self.fname = fname
        self.lname = lname
        self.country = country.capitalize()
        self.country_code = country
        self.phonenumber = phonenumber
        self.username = username
        self.password = password

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, f):
        if isinstance(f, str):
            self.__fname = f.capitalize()
        else:
            raise ValueError('fname Value Error')

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, l):
        if isinstance(l, str):
            self.__lname = l.capitalize()
        else:
            raise ValueError('lname Value Error')

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, c):
        if isinstance(c, str):
            code = getCountryCode(c)
            if code:
                self.__country_code = code
            else:
                raise ValueError('Country Value Error')
        else:
            raise ValueError('Country Value Error')

    @property
    def phonenumber(self):
        return self.__phonenumber

    @phonenumber.setter
    def phonenumber(self, ph):
        if isinstance(ph, str) and self.__country_code != '' and ph.isnumeric():
            if ph[0] == '+':
                self.__country_code, self.__phonenumber = ph.split(' ')
            else:
                self.__phonenumber = ph
        else:
            raise ValueError('phonenumber Value Error')

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, u):
        if isinstance(u, str) and u != '':
            self.__username = u
        else:
            raise ValueError('username Value Error')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, p):
        if isinstance(p, str) and p != '' and 8 < len(p) < 25:
            self.__password = md5(p.encode()).digest()
        else:
            raise ValueError('password Value Error')

    def __eq__(self, other):
        return all((self.username == other.username,
                    self.password, other.password))

    def __str__(self):
        return f"First Name : {self.fname}\n" + \
            f"Last Name : {self.lname}\n" + \
            f"Country : {self.country}\n" + \
            f"Phone Number : {self.country_code} {self.phonenumber}\n" + \
            f"Username : {self.username}\n" + \
            f"MD5 Password : {self.password}"

    def __repr__(self):
        return f"User({self.fname}, {self.lname}, {self.country}, {self.phonenumber}, {self.username}, {self.password})"
