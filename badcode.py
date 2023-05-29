from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT: int = 5


@dataclass
class Employee:
    """Basic representation of an employee at the company"""
    __name: str
    __role: str  # first code smell. it would be better to have fixed roles in the company (enums) since string can represent anything, and also it makes it more explicit
    __vacation_days: int = 25

    def getName(self) -> str:
        return self.__name

    def getRole(self) -> str:
        return self.__role

    def getVacationDays(self) -> int:
        return self.__vacation_days

    # code smell number 6: is adding two functionality to take_a_holiday method using the payout which is a bool as a condition;
    # paying out an employee should be separated from taking an holiday
    def take_a_holiday(self, payout: bool) -> None:
        """let the employee take a single holiday or payout 5 holidays"""
        if payout:
            # check that there are enough vacation days left for a payout
            if self.__vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"You don't have enough holidays left for a payout. Remaining holidays: {self.__vacation_days} should be more than 5 days")
            try:
                self.__vacation_days -= FIXED_VACATION_DAYS_PAYOUT # payout after every five days
                print(f"Paying out a holiday. Holidays left: {self.__vacation_days}")
            # code smell number 7:
            except Exception:
                # this is never happen
                pass
        else:
            if self.__vacation_days < 1:
                raise ValueError(f"You don't have any holidays left. Now back to work, you!")
            self.__vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails")


@dataclass
class HourlyEmployee(Employee):
    """ Employee that's paid based on number of hours worked """

    # code smell number four, using very vague identifier. This is very common among engineers. Take for example __amount, only I know what that is representing
    # to other developers, it might look like the actual amount being paid to the worker but I know it's the hours worked
    __hourly_rate: float = 50
    __amount: int = 10

    def getHourlyRate(self):
        return self.__hourly_rate

    def getAmount(self):
        return self.__amount


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    __monthly_salary: float = 5000

    def getMonthlySalary(self):
        return self.__monthly_salary


class Company:
    """Represents a company with employees."""

    __employees: List[Employee]

    def __init__(self):
        self.__employees: List[Employee] = []

    def getEmployees(self) -> List[Employee]:
        return self.__employees

    def getEmployee(self, index: int = None) -> Employee:
        return self.__employees[index]

    def addEmployee(self, employee: Employee) -> None:
        """Add an employee to the List of employees."""
        self.__employees.append(employee)

    # second code smell is duplicate type of code. there's actually no need to write different methods to get an employee based on their role
    # you'll notice the code all look alike except the role of the employee. If there was a bug with one method, then you'll have to fix it on the other methods
    # also imagine trying to find 50 categories of employees, that's 50 different methods to write
    def find_manager(self) -> List[Employee]:
        """Finds all the manager employees"""
        managers: List[Employee] = []
        # third code smell is not using builtin functions. This code looks fine but it can be better. How? we use list comprehension
        for employee in self.__employees:
            if employee.getRole() == "manager":
                managers.append(employee)
        return managers

    def find_vice_presidents(self) -> List[Employee]:
        """Finds all vice president employee"""
        vice_presidents: List[Employee] = []
        for employee in self.__employees:
            if employee.getRole() == "vice_president":
                vice_presidents.append(employee)
        return vice_presidents

    def find_interns(self) -> List[Employee]:
        """Finds all interns employee"""
        interns: List[Employee] = []
        for employee in self.__employees:
            if employee.getRole() == "intern":
                interns.append(employee)
        return interns

    # number five code smell; putting the pay method in the Company class could be there, but shouldn't be, why?
    # Imagine having to check every instance of an employee before you can carry out a task
    # anytime you see isinstance is many places in your code, an alarm bell should tick off
    # it also means that if a new type of employee or a new category of an employee is added, we'd need to add another conditions
    @staticmethod
    def pay_employee(employee: Employee):
        """Pay an employee"""
        if isinstance(employee, SalariedEmployee):
            print(f"Paying Employee {employee.getName()} a monthly salary {employee.getMonthlySalary()}")
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.getName()} a hourly rate of ${employee.getHourlyRate()} for {employee.getAmount()} hours")
