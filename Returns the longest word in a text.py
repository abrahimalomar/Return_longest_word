

def get_longest_word(text):
    longest_word = " "
    word_list = text.split(" ")
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

txt = "This is a test sentence to find the longest word in the text"
print(get_longest_word(txt))


 