import random
import sys
from typing import List, Any


def generate_random_sentence(input_sentence: str) -> str:
    """
    main function which takes the input sentence as a parameter and returns the replacement sentence
    :param input_sentence: a string containing the input sentence
    :return: a string containing the replacement sentence
    """
    word_arr = get_word_list()
    word_dict = divide_list(lst=word_arr)
    replacement_arr = get_replacement_words(input_sentence=input_sentence, word_dict=word_dict)
    result = ' '.join(replacement_arr)
    return result


def get_word_list() -> list:
    """
    function to get the stored word list as provided by http://www.mieliestronk.com/corncob_lowercase.txt and return it as an arry
    :return: an array containing all the words in the file provided
    """
    # import word list
    my_file = open('words.txt', 'r')
    # read text file into list
    data = my_file.read()
    arr = data.split('\n')
    return arr


def get_replacement_words(input_sentence: str, word_dict: List[list]) -> list:
    """
    function to iterate through each word in the input sentence and randomly find a word of the same length and starting with the same letter
    :param input_sentence: a string containing the input sentence
    :param word_dict: a list of list containing the word options, list is segregated according to word length
    :return: a list containing the replacement words for the given input sentence
    """
    string_list = list(input_sentence.split(' '))
    output = []
    for i in range(len(string_list)):
        word = string_list[i]
        if len(word) < 2 or len(word) > 22:
            raise AttributeError('Word ' + word + ' is of non-viable length')
        else:
            option_list = [i for i in word_dict[len(word) - 1] if i.startswith(word[0])]
            replacement_word = random.choice(option_list)
            output.append(replacement_word)
    return output


def divide_list(lst: list) -> List[List[Any]]:
    """
    function that divides a given unsorted array into a list of list, with words being grouped by length
    :param lst: a list containing all available words
    :return: a list of lists, segregated by word length
    """
    dct = {}

    for element in lst:
        if len(element) not in dct:
            dct[len(element)] = [element]
        elif len(element) in dct:
            dct[len(element)] += [element]

    res = []
    for key in sorted(dct):
        res.append(dct[key])

    return res


return_sentence = generate_random_sentence(sys.argv[1])
print(return_sentence)
