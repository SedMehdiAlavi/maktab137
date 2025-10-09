def write_file(filename):
    with open(filename,'w') as file:
        file.write("hello world\nHow are you?\nwellcome!")
    with open('q4.txt','r') as file:
        for line in file:
            print(line)

write_file('q4.txt')