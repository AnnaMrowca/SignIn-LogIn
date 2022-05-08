import os

folder_path = r'C:\Users\Ania\PycharmProjects\SignIn-LogIn'
file_path = os.path.join(folder_path, 'base.txt')

class SignIn:

    def __init__(self):
        self.email = input('Enter your email: ')
        self.password = input('Enter your password: ')


    def sign_in(self):

        if os.path.exists(file_path) == False:
            with open(file_path, 'a') as file:
                file.write(self.email + ' ' + self.password + '\n')
            return 'Successful sign-in.'


        elif os.path.exists(file_path) == True:
            with open(file_path, 'r+',) as file:
                lines = file.read().splitlines()

                for line in lines:
                    if self.email not in line.split(' ')[0]:
                        file.write(self.email + ' ' + self.password + '\n')
                        return' Successful sign-in.'

                    else:
                        return 'This email already in use. Try different email'


class LogIn(SignIn):

    # def __init__(self):
    #     super().__init__() - zbędne

    def log_in(self):
        with open(file_path, 'r') as base_directory:
            lines = base_directory.read().splitlines()
            if self.email + ' ' + self.password in lines:
                return 'Successful login.'
            return 'Wrong email or password. Try again'


choice = 1

while choice != 3:
    choice = int(input('''
                       1 - sign in
                       2 - log in
                       3 - end program
                       : '''))

    if choice == 1:
        new_user = SignIn()
        print(new_user.sign_in())


    elif choice == 2:

            logged_user = LogIn()
            print(logged_user.log_in())


    else:
        print('End of program.')