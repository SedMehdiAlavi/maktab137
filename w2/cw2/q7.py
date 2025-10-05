import csv

def list_csv(filename):
    with open(filename, 'w') as file:
        file.write('name, age, score\n')
        file.write('Ali, 23, 19\n')
        file.write('Ahmad, 45, 17\n')
        file.write('Mehran, 32, 15\n')
    with open(filename, 'r') as file:
        file.read()


list_csv('q7.csv')