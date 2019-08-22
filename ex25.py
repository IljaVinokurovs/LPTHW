def break_words(stuff):
    #thess """ """ strings are used to write help info in the code, similar to comments, but you can see them within reminal
    """This funtion will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the forst word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last workd after popping it off."""
    word = words.pop()
    print(word)

def sort_sentence(sentence):
    """Takes in full sentence and returns sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first and last one."""
    print_first_word(sort_sentence(sentence))
    print_last_word(sort_sentence(sentence))
