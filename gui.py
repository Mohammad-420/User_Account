from tkinter import *
from user import User
from country_code_checker import getCountryCode

FONT_CHARECTER = 'Arial'
FONT_SIZE = 18
FONT = (FONT_CHARECTER, FONT_SIZE)

MARGIN = 5


class SignUp(Frame):
    def __init__(self, parent, countries=('iran', 'usa')):
        super(SignUp, self).__init__(parent)

        self.countries = sorted(countries)

        self.__fname = StringVar(self)
        self.__lname = StringVar(self)
        self.__username = StringVar(self)
        self.__country = StringVar(self, getCountryCode('iran'))
        self.__phonenumber = StringVar(self)
        self.__password = StringVar(self)
        self.__showpasswd = IntVar(self)

        # First Name
        Label(self, text='First Name', font=FONT).grid(
            row=0, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        Entry(self, font=FONT, textvariable=self.__fname).grid(
            row=0, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # Last Name
        Label(self, text='Last Name', font=FONT).grid(
            row=1, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        Entry(self, font=FONT, textvariable=self.__lname).grid(
            row=1, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # phone number & country
        Label(self, text='Phone Number', font=FONT).grid(
            row=2, column=0, sticky='w', padx=MARGIN, pady=MARGIN)

        country = Menubutton(self, text=getCountryCode('iran'), font=(FONT_CHARECTER, 13))
        country.grid(row=2, column=1, sticky='w', padx=MARGIN, pady=MARGIN)

        country.menu = Menu(country, tearoff=0)
        country['menu'] = country.menu

        def set_country_code():
            c = getCountryCode(self.__country.get())
            country.config(text=c)

        for c in self.countries:
            country.menu.add_radiobutton(
                label=c.capitalize(), value=c.lower(), variable=self.__country, command=set_country_code)

        Entry(self, font=FONT, textvariable=self.__phonenumber, width=15).grid(
            row=2, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # Username
        Label(self, text='Username', font=FONT).grid(
            row=3, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        Entry(self, font=FONT, textvariable=self.__username).grid(
            row=3, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # Password
        Label(self, text='Password', font=FONT).grid(
            row=4, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        passwd = Entry(self, font=FONT, show='*', textvariable=self.__password)
        passwd.grid(row=4, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # show Password
        Checkbutton(self, text='Show Password', font=FONT, variable=self.__showpasswd, offvalue=0,
                    onvalue=1, command=lambda: self.__showPasswd(passwd)).grid(row=5, column=0, sticky='w', padx=MARGIN, pady=MARGIN)

        # submit
        Button(self, text='submit', font=FONT, command=self.__create_user).grid(
            row=6, column=1, columnspan=2)

    def __clear(self):
        self.__fname.set('')
        self.__lname.set('')
        self.__phonenumber.set('')
        self.__username.set('')
        self.__password.set('')

    def __create_user(self):
        import pickle
        f, l, u, p, c, ph = (self.__fname.get(), self.__lname.get(),
                             self.__username.get(), self.__password.get(),
                             self.__country.get(), self.__phonenumber.get())
        self.__clear()
        user = User(fname=f, lname=l, username=u,
                    password=p, country=c, phonenumber=ph)
        try:
            with open('users.txt', 'rb') as f:
                users = pickle.load(f)
        except:
            users = []
        with open('users.txt', 'wb') as f:
            users.append(user)
            pickle.dump(users, f)
        # exit()

    def __showPasswd(self, passwd):
        if self.__showpasswd.get():
            passwd.config(show='')
        else:
            passwd.config(show='*')


class Login(Frame):
    def __init__(self, parent):
        super(Login, self).__init__(parent)

        self.__username = StringVar(self)
        self.__password = StringVar(self)
        self.__showpasswd = IntVar(self)

        # username
        Label(self, text='Username', font=FONT).grid(
            row=0, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        Entry(self, font=FONT, textvariable=self.__username).grid(
            row=0, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # password
        Label(self, text='Password', font=FONT).grid(
            row=1, column=0, sticky='w', padx=MARGIN, pady=MARGIN)
        passwd = Entry(self, font=FONT, show='*', textvariable=self.__password)
        passwd.grid(row=1, column=1, sticky='e', padx=MARGIN, pady=MARGIN)

        # show password
        Checkbutton(self, text='Show Password', font=FONT, variable=self.__showpasswd, offvalue=0,
                    onvalue=1, command=lambda: self.__showPasswd(passwd)).grid(row=2, column=0, sticky='w', padx=MARGIN, pady=MARGIN)

        # submit
        Button(self, text='Submit', font=FONT, command=self.__find_user).grid(
            row=3, column=1, columnspan=2, padx=MARGIN, pady=MARGIN)

    def __clear(self):
        self.__username.set('')
        self.__password.set('')

    def __find_user(self):
        import pickle
        u, p = self.__username.get(), self.__password.get()
        self.__clear()
        requested_user = User(username=u, password=p)
        with open('users.txt', 'rb') as f:
            users = pickle.load(f)
            for user in users:
                if user == requested_user:
                    print('Login Successfully ... ')
                    print(repr(user))
                    # exit()

    def __showPasswd(self, passwd):
        if self.__showpasswd.get():
            passwd.config(show='')
        else:
            passwd.config(show='*')


class MainPage(Tk):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        menubar = Menu(self)
        menubar.add_command(
            label='Login', command=lambda: self.show_frame('Login'))
        menubar.add_command(
            label='SignUp', command=lambda: self.show_frame('SignUp'))

        self.config(menu=menubar)

        self.frames = {}

        for f in (SignUp, Login):
            page_name = f.__name__
            frame = f(self)
            self.frames[page_name] = frame

        self.show_frame('SignUp')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.title(page_name)
        if page_name == 'SignUp':
            self.frames['Login'].grid_forget()
        elif page_name == 'Login':
            self.frames['SignUp'].grid_forget()
        frame = self.frames[page_name]
        frame.grid(row=0, column=0)


if __name__ == "__main__":
    m = MainPage()
    m.mainloop()
