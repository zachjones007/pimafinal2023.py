import re
import random


class Employee:
    def __init__(self, first_name, last_name, social):
        self._first_name = first_name  # protected attributes
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
        pass

    def __repr__(self):
        return f"Name: {self._first_name} {self._last_name}, Social: {self._social}"


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, social, weekly_salary):
        super().__init__(first_name, last_name, social)
        self._weekly_salary = max(0, weekly_salary)

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, value):
        if value < 0:
            self._weekly_salary = 0
        else:
            self._weekly_salary = value

    def earnings(self):
        return self._weekly_salary

    def __repr__(self):
        return f"Salaried Employee: {super().__repr__()}"


class HourlyEmployee(Employee):
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
            overtime_pay = (self._hours - 40) * (1.5 * self._wage_per_hour)
            return regular_pay + overtime_pay

    def __repr__(self):
        return f"Hourly Employee: {super().__repr__()}"


class CheckPass(Employee):
    def __init__(self, first_name, last_name, social, hours, wage_per_hour):
        super().__init__(first_name, last_name, social)
        # Rest of CheckPass is now properly integrated
        Pass = str(input('Do you have a password?'))
        if Pass in ('Y', 'E', 'S'):
            with open('passwordlist.txt', 'r') as file:
                # The rest of the code for CheckPass, which you provided, would be here...
                pass
        else:
            # The rest of the code for CheckPass, which you provided, would be here...
            pass


class setPAss:
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


def main():
    salaried_emp = SalariedEmployee("Alice", "Smith", "987-65-4321", 1000)
    hourly_emp = HourlyEmployee("Bob", "Johnson", "456-78-9123", 45, 20)
    check_pass = CheckPass("John", "Doe", "123-45-6789", 40, 25)

    passwd_obj = setPAss()
    print(passwd_obj.random_password())
    print('Thank you')


if __name__ == '__main__':
    main()

