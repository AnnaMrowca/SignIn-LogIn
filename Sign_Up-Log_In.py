import os

folder_path = r'C:\Users\Ania\PycharmProjects\SignIn-LogIn'
file_path = os.path.join(folder_path, 'base.txt')


class SignUp:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def sign_up(self):
            with open(file_path, 'a') as file:
                file.write(self.email + ' ' + self.password + '\n')


    def check_email(self):
        if os.path.exists(file_path) == True:
            with open(file_path, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    if self.email in line.split(' ')[0]:
                        return True
                return False
        else:
            return False


class LogIn(SignUp):

    def log_in(self):
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                if self.email in line.split(' ')[0] and self.password in line.split(' ')[1]:
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
                print('Email already exists. Try again or go to log in')
        else:
            print('Your passwords do not match')

    elif choice == 2:
        email = input('Enter your email: ')
        password = input('Enter your password: ')

        account = LogIn(email, password)
        if account.check_email() == True:
            account.log_in()
            print('Sucessful login')
        else:
            print('Email does not exist in database')

    else:
        print('End of program.')





