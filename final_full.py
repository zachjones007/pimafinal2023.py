import csv
from ping3 import ping
import ezgmail
import random
import logging

logging.basicConfig(filename='automation_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class Employee:
    def __init__(self, first_name, last_name, social, hours):
        self._first_name = first_name
        self._last_name = last_name
        self._social = social
        self._hours = hours

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def social(self):
        return self._social

    @property
    def hours(self):
        return self._hours

    def earnings(self):
        pass

    def __repr__(self):
        overtime_status = "Overtime" if self._hours == "1" else "Regular"
        return f"Name: {self._first_name} {self._last_name}, Social: {self._social}, Status: {overtime_status}"

def password_strength(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    special_characters = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '!']
    if not any(char in special_characters for char in password):
        return False
    return True

class PasswordChecker(Employee):
    def check_password(self):
        x = 0
        doyouhaveanemail = input("do you have an email?")
        has_user = input('Enter your email: ')
        with open('generated_passwords.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                username, password, hours = row
                if has_user == username:
                    employee = Employee(username, "", "", hours)
                    print(employee)
                    has_pass = input('Enter your password: ')
                    if has_pass == password:
                        print("Password matched!")
                    elif x == 4:
                        print("Incorrect password!")
                        print('sending password recovery to your email' )
                        ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')
                        ipFile = open('ip.csv')
                        ipReader = csv.DictReader(ipFile)
                        msg = "Someone may have tried accessing your account. Here's a ping check:\n\n"
                        for row in ipReader:
                            ip = row['ip']
                            ping_time = ping(ip)
                            msg += f"{ip}: {ping_time}\n"
                        ipFile.close()
                        subject = "Someone could be trying to get into your account"
                        ezgmail.send(username, subject, msg)
                    else: 
                        print("Password is incorrect")
                        x += 1 
                    break
            else:
                print("Username not found!")

class PasswordGenerator:
    def __init__(self, item_mapping=None):
        self.item_mapping = item_mapping or {
            1: {"name": 'A'},
            2: {"name": 'B'},
            3: {"name": 'C'},
            4: {"name": 'D'},
            5: {"name": 'E'},
            6: {"name": 'F'},
            7: {"name": 'G'},
            8: {"name": 'H'},
            9: {"name": 'I'},
            10: {"name": 'J'},
            11: {"name": 'K'},
            12: {"name": 'L'},
            13: {"name": 'M'},
            14: {"name": 'N'},
            15: {"name": 'O'},
            16: {"name": 'P'},
        }

    def random_password(self):
        password = []
        for _ in range(10):
            item_number = random.randint(1, 16)
            item_name = self.item_mapping[item_number]["name"]
            password.append(item_name)
        return ''.join(password)

    def write_password_to_file(self, email, password, hours):
        with open('generated_passwords.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, password, hours])
        logging.info(f'Generated password for {email} and saved to file.')

def main():
    passwd_gen = PasswordGenerator()
    email = input('Enter email to generate password for: ')
    hours_worked = int(input('Enter the number of hours worked: '))
    employee_type = "1" if hours_worked > 40 else "0"
    random_pass = passwd_gen.random_password()
    while not password_strength(random_pass):
        random_pass = passwd_gen.random_password()
    passwd_gen.write_password_to_file(email, random_pass, employee_type)
    print(f"Generated strong password for {email}: {random_pass}")
    password_checker = PasswordChecker("John", "Doe", "123-45-6789", hours=employee_type)
    password_checker.check_password()
    print('Thank you')

if __name__ == '__main__':
    main()
