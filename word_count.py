def word_count_items(string):
    """ counts the occurences or characters in a word"""
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)
word_count_items("I am a girl with a good heart")


