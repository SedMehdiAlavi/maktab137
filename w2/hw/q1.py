import csv
import json

#part1
def reading():
    with open('maktab137.hw.log', 'r') as file:
        file.readline()

#part2
def extractor():
    with open('maktab137.hw.log', 'r') as file:

        for line in file:

            try:
                content = line.split()
                if content[5] == '[error]' or content[5] == '[notice]':
                    timestamp = f'{content[0]} {content[1]} {content[2]} {content[3]} {content[4]}'.replace('[', '').replace(']', '')
                    level = f'{content[5]}'.replace('[', '').replace(']', '')
                    message = ' '.join(content[6:])
                    print(f'[{timestamp}] [{level}] {message}')


            except IndexError:
                continue

#part3
def error_detector():
    c = 0
    with open('error.log', 'w') as file:
        pass
    with open('maktab137.hw.log', 'r') as file:

        for line in file:
            content = line.split()
            c += 1
            try:
                if content[5] != '[error]' and content[5] != '[notice]':
                    with open('error.log', 'a') as error:
                        error.write(f'{c} : {line}')

            except IndexError:
                with open('error.log', 'a') as error:
                    error.write(f'{c} : {line}')

#part4
def error_extractor():
    with open('maktab137.hw.log', 'r') as file:

        with open('critical_error.csv', 'w', newline='', encoding='utf-8') as critical:
            time = ('Timestamp')
            mess = ('Message')
            column = ((time), (mess))
            writer1 = csv.writer(critical)
            writer1.writerow(column)

        for line in file:
            try:
                content = line.split()

                if content[5] == '[error]':
                    timestamp = ' '.join(content[0:5])
                    message = ' '.join(content[6:])

                    with open('critical_error.csv', 'a', newline='', encoding='utf-8') as critical:
                        writer2 = csv.writer(critical)
                        writer2.writerow((timestamp, message))


            except IndexError:
                continue



#part5
def sum_logs():
    with open('maktab137.hw.log', 'r') as file:
        info = []
        warning = []
        error = []
        for line in file:

            content = line.split()
            try:

                if content[5] == '[notice]':
                     info.append('info')

                elif content[5] != '[notice]' and content[5] != '[error]':
                    warning.append('warning')

                elif content[5] == '[error]':
                    error.append('error')



            except IndexError:
                warning.append('warning')

        info_counter = str(info.count('info'))
        warning_counter = str(warning.count('warning'))
        error_counter = str(error.count('error'))

        data = {"INFO" : info_counter, "WARNING": warning_counter, "ERROR": error_counter}

        with open('summary.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent= 0)

#part6
try:
    with open('server.log', 'r') as file:
        file.readline()

except FileNotFoundError as error:
    print(error)

    extractor()
    error_detector()
    error_extractor()
    sum_logs()


