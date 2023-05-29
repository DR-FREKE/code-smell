# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from badcode import Company, SalariedEmployee, HourlyEmployee


def main() -> None:
    """main function to call employee function"""
    company = Company()
    print("input x if you want to cancel the program")
    staff_number = input("please provide number of staff you wish to add to your company: ")

    while staff_number != "x":
        for i in range(int(staff_number)):
            employee_name = input("please provide an employee name: ")

            print(f"select 1 to assign a vice_president role for this employee")
            print(f"select 2 to assign a manager role for this employee")
            print(f"select 3 to assign an intern role for this employee")

            employee_role = int(input("select a number: "))
            role: str

            if employee_role == 1:
                role = "vice_president"
            elif employee_role == 2:
                role = "manager"
            else:
                role = "intern"
            company.addEmployee(SalariedEmployee(employee_name, role))

        print(company.find_vice_presidents())
        print(company.find_manager())
        print(company.find_interns())

        company.pay_employee(company.getEmployee(0))
        company.getEmployee(0).take_a_holiday(False)

        if int(staff_number) <= len(company.getEmployees()):
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
