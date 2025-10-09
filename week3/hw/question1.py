import itertools
import copy

#part1
input_word = input("Enter yor words: ")
words = input_word.split()

def combining_words():
    """
    We want to collect all permutations of user input I named 'input_word'.

    It's a generator function, so we need call it multiple times to yield all permutations.
    The built-in permutations function creates a list of tuples. If we want to change an element
        in tuples, we need convert them into lists with 'list()' function. I assign empty lists
        to append tuples after converting them into lists .

    """

    binary = list(itertools.permutations(words, 2))
    binary_word_list = []
    for i in binary:
        binary_word_list.append(list(i))
    yield binary_word_list


    triple = list(itertools.permutations(words, 3))
    triple_word_list = []
    for i in triple:
        triple_word_list.append(list(i))
    yield triple_word_list


    quadruple = list(itertools.permutations(words, 4))
    quadruple_word_list = []
    for i in quadruple:
        quadruple_word_list.append(list(i))
    yield quadruple_word_list

combined_words = combining_words()

main_double = next(combined_words)
main_triple = next(combined_words)
main_quad = next(combined_words)

shall_double = copy.copy(main_double)
shall_triple = copy.copy(main_triple)
shall_quad = copy.copy(main_quad)

deep_double = copy.deepcopy(main_double)
deep_triple = copy.deepcopy(main_triple)
deep_quad = copy.deepcopy(main_quad)

main_double[0][0] = "maktab137"


print('original'.center(50, '-'))
print(main_double)
print(main_triple)
print(main_quad)

print('shallow'.center(50, '-'))
print(shall_double)
print(shall_triple)
print(shall_quad)

print('deep'.center(50, '-'))
print(deep_double)
print(deep_triple)
print(deep_quad)