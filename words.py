def print_upper_words(words):
    """convert each word in the given list to uppercase and print out each word on separate line."""

    for word in words:
        print(word.upper(), end = "\n")
    
print_upper_words(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"])


def print_upper_words_start_e(words):
    """convert word in the given list to uppercase and print out each word on separate line if words start with letter 'e'."""

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper(), end = "\n")
    
print_upper_words_start_e(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"])


def print_upper_words_start_letters(words, must_start_with):
    """convert word in the given list to uppercase and print out each word on separate line if words start with given letter."""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper(), end = "\n")
                break
        
    
print_upper_words_start_letters(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"] , must_start_with={"R", "c"} )
print_upper_words_start_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})