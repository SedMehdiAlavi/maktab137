from copy import deepcopy

def caching(func):
    cache = {}
    def wrapper(word , count):
        key = str(count)
        if key in cache:
            print("Cache hit")
            return deepcopy(cache[key])

        result = func(word, count)
        cache[key] = deepcopy(result)
        print("Cache created")
        return result

    return wrapper


@caching
def repeat_counter(sentence, counter):
    """
    In this function, we want to count the number of times
     the specified-words user input is repeated.
    After collect input, we will check existing punctuation marks in
     a for loop to remove every punctuation marks, then we lower
     every letter, then we put the words into a list.
    Now we can count the specified_words with 'count' method.
    Finally, function returns a f-string of specified-word and the
    number of repeating.
    """

    punctuations = "!@#$%^&*()_+-={}[]:;'<>?,./"

    for word in sentence:
        if word in punctuations:
            sentence = sentence.replace(word, "")
        else:
            sentence = sentence.lower()
    words = sentence.split()

    repeat_number = {}


    for word in counter:
        repeat_number[word] = words.count(word)


    return repeat_number


print(repeat_counter("sed mehdi alavi sed sed sed mehdi mehdi alavi mehdi", ["sed", "mehdi", "alavi"]))
print(repeat_counter("sed mehdi alavi sed sed sed mehdi mehdi alavi mehdi", ["sed", "mehdi", "alavi"]))


print(repeat_counter("sed mehdi alavi sed mehdi", ["sed", "mehdi"]))
print(repeat_counter("sed mehdi alavi sed mehdi", ["sed", "mehdi"]))

print(repeat_counter("sed mehdi alavi sed sed sed mehdi mehdi alavi mehdi", ["sed", "mehdi", "alavi"]))

print(repeat_counter(" alavi sed sed sed mehdi ", ["sed", "mehdi", "alavi"]))
print(repeat_counter(" alavi sed sed sed mehdi ", ["sed", "mehdi", "alavi"]))
print(repeat_counter("sed mehdi alavi sed sed sed mehdi mehdi alavi mehdi", ["sed", "mehdi", "alavi"]))
print(repeat_counter("sed mehdi alavi sed sed sed mehdi mehdi alavi mehdi", ["sed", "mehdi", "alavi"]))

