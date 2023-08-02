import csv
from ping3 import ping
import ezgmail
import random

class Employee:
    """Base class for all types of employees."""
    
    def __init__(self, first_name, last_name, social):
        self._first_name = first_name
        self._last_name = last_name
        self._social = social

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def social(self):
        return self._social

    def earnings(self):
        """Method to calculate earnings for the employee."""
        pass

    def __repr__(self):
        return f"Name: {self._first_name} {self._last_name}, Social: {self._social}"

class SalariedEmployee(Employee):
    """Class to represent employees with a fixed weekly salary."""
    
    def __init__(self, first_name, last_name, social, weekly_salary):
        super().__init__(first_name, last_name, social)
        self._weekly_salary = max(0, weekly_salary)

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value):
        self._weekly_salary = max(0, value)

    def earnings(self):
        return self._weekly_salary

    def __repr__(self):
        return f"Salaried Employee: {super().__repr__()}"

class HourlyEmployee(Employee):
    """Class to represent employees who are paid based on hourly wages."""
    
    def __init__(self, first_name, last_name, social, hours, wage_per_hour):
        super().__init__(first_name, last_name, social)
        self._hours = max(0, hours)
        self._wage_per_hour = max(0, wage_per_hour)

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = max(0, value)

    @property
    def wage_per_hour(self):
        return self._wage_per_hour

    @wage_per_hour.setter
    def wage_per_hour(self, value):
        self._wage_per_hour = max(0, value)

    def earnings(self):
        if self._hours <= 40:
            return self._hours * self._wage_per_hour
        else:
            regular_pay = 40 * self._wage_per_hour
            overtime_pay = (self._hours - 40) * 1.5 * self._wage_per_hour
            return regular_pay + overtime_pay

    def __repr__(self):
        return f"Hourly Employee: {super().__repr__()}"

class PasswordChecker(Employee):
    """Class to represent employees who can check passwords."""
    
    def check_password(self):
        x = 0
        doyouhaveanemail = input("do you have an email?")
        has_user = input('Enter your email: ')
        with open('generated_passwords.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                username, password = row
                if has_user == username:
                    has_pass = input('Enter your password: ')
                    if has_pass == password:
                        print("Password matched!")
                    elif x == 4:
                        print("Incorrect password!")
                        print('sending password recovery to your email' )
                        ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')

                        # Open the CSV file and read IP addresses
                        ipFile = open('ip.csv')
                        ipReader = csv.DictReader(ipFile)
                        msg = "Someone may have tried accessing your account. Here's a ping check:\n\n"
                        for row in ipReader:
                            ip = row['ip']
                            ping_time = ping(ip)
                            msg += f"{ip}: {ping_time}\n"
                        # Close the CSV file
                        ipFile.close()

                        # Send the email
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

    def write_password_to_file(self, email, password):
        with open('generated_passwords.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, password])

def main():
    passwd_gen = PasswordGenerator()
    email = input('Enter email to generate password for: ')
    random_pass = passwd_gen.random_password()
    passwd_gen.write_password_to_file(email, random_pass)
    print(f"Generated password for {email}: {random_pass}")

    password_checker = PasswordChecker("John", "Doe", "123-45-6789")
    password_checker.check_password()

    print('Thank you')

if __name__ == '__main__':
    main()

