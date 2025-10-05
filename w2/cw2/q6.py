def count_words(filename, words):
    with open(filename, 'w') as file:
        file.write(words)

    with open(filename, 'r') as file:
        content = file.read()
        word = content.split()
        count = len(word)
        print(count)


count_words('q6.txt', "apple baby cat dog hot")