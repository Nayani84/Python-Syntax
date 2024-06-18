def print_upper_words(words):
    """convert each word in the given list to uppercase and print out each word on separate line.

     For example:

      print_upper_words(["bear", "Dog", "eagle", "cat"])

    should print:
        BEAR
        DOG
        EAGLE
        CAT

    """

    for word in words:
        print(word.upper(), end = "\n")

print("*****print_upper_words*****")  
print_upper_words(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"])





def print_upper_words_start_e(words):
    """convert word in the given list to uppercase and print out each word on separate line if words start with letter 'e'.
    
    For example:

      print_upper_words_start_e(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"])

    should print:
        EAGLE
        ELEPHANT
    """

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper(), end = "\n")

print("*****print_upper_words_start_e*****")   
print_upper_words_start_e(["bear", "Dog", "eagle", "cat", "Rabbit", "squirrel", "Hamster", "Elephant"])





def print_upper_words_start_letters(words, must_start_with):
    """convert word in the given list to uppercase and print out each word on separate line if words start with given letter.

    For example:
        print_upper_words_start_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

     should print:   
        HELLO
        HEY
        YO
        YES
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper(), end = "\n")
                break

print("*****print_upper_words_start_letters*****")       
print_upper_words_start_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})