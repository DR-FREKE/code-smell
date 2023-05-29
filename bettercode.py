from dataclasses import dataclass
from typing import List
from enum import Enum, auto
from abc import ABC, abstractmethod

FIXED_VACATION_DAYS_PAYOUT: int = 5


class Role(Enum):
    """Employee roles."""
    PRESIDENT = auto()
    VICE_PRESIDENT = auto()
    MANAGER = auto()
    INTERN = auto()


class Payroll:
    """Basic representation of an employee payroll"""
    __housing: float
    __transport: float
    __basic: float
    __tax_percent: float = 2.5

    def __init__(self, housing: float, transport: float, basic: float):
        self.__housing = housing
        self.__transport = transport
        self.__basic = basic

    def calculate_tax(self):
        """calculates tax amount from the employee salary using the tax percent"""
        pass

    def calculate_gross(self):
        """ calculates the total earnings of the employee for the month (before tax deduction)"""
        pass

    def calculate_net(self):
        """calculates the total earning of an employee for the month (after tax deduction)"""
        pass


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company"""
    __name: str
    __role: Role
    payroll: Payroll
    __vacation_days: int = 25

    def getName(self) -> str:
        return self.__name

    def getRole(self) -> Role:
        return self.__role

    def getVacationDays(self) -> int:
        return self.__vacation_days

    def take_a_holiday(self) -> None:
        """let the employee take a single holiday."""
        if self.__vacation_days < 1:
            raise ValueError(f"You don't have any holidays left. Now back to work, you!")
        self.__vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails")

    def payout_a_holiday(self) -> None:
        """Let the employee get paid for unused holiday"""
        # check that there are enough vacation days left for a payout
        if self.__vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"You don't have enough holidays left for a payout. Remaining holidays: {self.__vacation_days}")
        try:
            self.__vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            print(f"Paying out a holiday. Holidays left: {self.__vacation_days}")
        except Exception:
            # this is never happen
            pass

    @abstractmethod
    def pay(self) -> None:
        """for paying employees"""


@dataclass
class HourlyEmployee(Employee):
    """ Employee that's paid based on number of hours worked """

    __hourly_rate: float = 50
    __hours_worked: int = 10

    def getHourlyRate(self):
        return self.__hourly_rate

    def getHoursWorked(self):
        return self.__hours_worked

    def pay(self) -> None:
        print(
            f"Paying employee {self.getName()} a hourly rate of ${self.getHourlyRate()} for {self.getHoursWorked()} hours")


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    __monthly_salary: float = 5000

    def getMonthlySalary(self):
        return self.__monthly_salary

    def pay(self) -> None:
        print(f"Paying Employee {self.getName()} a monthly salary {self.getMonthlySalary()} using payroll of {self.payroll.calculate_net()}")


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

    def find_employee(self, role: Role) -> List[Employee]:
        """Finds employees with a particular role using list comprehension"""
        return [employee for employee in self.__employees if employee.getRole() is role]
