def salary_calculator (basesalary):
	numofweeks = 52
	numhours = 40
	return (basesalary / numofweeks) / (numhours)
	
	
def hourly_calculator (hourlywage):
	numofweeks = 52
	numhours = 40
	return (hourlywage * numhours) * numofweeks
	
	
	
print (hourly_calculator(24.04))
print (salary_calculator(50000))
print (f'The hourly rate for a person making $50,000 a year would be ${round(salary_calculator(50000), 2)}')
print (f'The annual salary for a person making $24.04 per an hour is ${int(round(hourly_calculator(24.04)))}')