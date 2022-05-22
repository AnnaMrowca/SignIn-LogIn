import os

folder_path = r'C:\Users\Ania\PycharmProjects\SignIn-LogIn'
file_path = os.path.join(folder_path, 'base.txt')


class SignUp:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_email(self):
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                if self.email in line.split(' ')[0]:
                    return True
            return False

    def sign_up(self):
        with open(file_path, 'a') as file:
            file.write(self.email + ' ' + self.password + '\n')

class LogIn(SignUp):

    def log_in(self):
        if SignUp.check_email(self) == True:
            return True
        return False



choice = 1

while choice != 3:
    choice = int(input('''
                       1 - sign in
                       2 - log in
                       3 - end program
                       : '''))

    if choice == 1:

        email = input('Enter your email: ')
        password = input('Enter your password: ')
        repeat_password = input('Repeat your password: ')

        if repeat_password == password:
            account = SignUp(email, password)
            if account.check_email() == False:
                account.sign_up()
                print('Successful sign-in.')
            else:
                print('This email already in use. Try different email')

    elif choice == 2:
        email = input('Enter your email: ')
        password = input('Enter your password: ')

        account = LogIn(email, password)
        if account.log_in() == True:
            print('Successful login')
        else:
            print('Email does not exist in our database. Use sign-up option')

    else:
        print('End of program.')





