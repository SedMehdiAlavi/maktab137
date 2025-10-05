def reading_file(filename):
    with open(filename, 'w') as file:
        file.write("123456789123456789123456789")

    with open(filename, 'r') as file:
        content = file.read(20)
        print(content)


reading_file('q5.txt')