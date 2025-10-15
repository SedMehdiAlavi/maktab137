from itertools import groupby
employees = [
    {'name': 'Ali', 'department': 'HR'},
    {'name': 'Sara', 'department': 'Engineering'},
    {'name': 'Reza', 'department': 'HR'},
    {'name': 'Maryam', 'department': 'Engineering'},
    {'name': 'Nima', 'department': 'Sales'},
    {'name': 'Hadi', 'department': 'Sales'}
]

sorted_employees = sorted(employees, key = lambda x: x['department'])
for key, group in groupby(sorted_employees, lambda x: x['department']):
    names = [employee['name'] for employee in group]
    print(f"Department: {key} -> {names}")

