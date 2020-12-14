from datetime import date

people = dict()
people['name'] = str(input('Name: '))
year_birth = int(input('Year of birth: '))
people['age'] = date.today().year - year_birth
people['ctps'] = int(input('Word card (0 not have): '))
if people['ctps'] != 0:
    people['year_hiring'] = int(input('Year of hiring: '))
    people['salary'] = float(input('Salary: R$ '))
    people['retires'] = (people['year_hiring'] - year_birth) + 35 
print('=-' * 20)
for k, v in people.items():
    print(f'{k} have the value {v}')