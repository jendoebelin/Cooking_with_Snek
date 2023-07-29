# Declare constants
NUM_OF_WEEKS = 52
NUM_HOURS = 40

def salary_calculator(basesalary):
    """Calculate hourly rate from base salary.

    Args:
    basesalary: Base annual salary.

    Returns:
    Hourly wage equivalent of the base salary.
    """
    return round(basesalary / NUM_OF_WEEKS / NUM_HOURS, 2)


def hourly_calculator(hourlywage):
    """Calculate annual salary from hourly wage.

    Args:
    hourlywage: Hourly wage.

    Returns:
    Base salary equivalent of the hourly wage.
    """
    return round(hourlywage * NUM_HOURS * NUM_OF_WEEKS, 2)


def main():
    basesalary = float(input("What is your base salary?"))
    hourlywage = float(input("What is your hourly wage to the nearest cent?"))

    print(f'The hourly rate for a person making {basesalary} a year would be ${salary_calculator(basesalary)}')
    print(f'The annual salary for a person making {hourlywage} per an hour is ${hourly_calculator(hourlywage)}')


# Start the program
if __name__ == "__main__":
    main()
