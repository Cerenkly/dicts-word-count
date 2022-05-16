"""Count words in file."""

def word_count(file):
    test_text = open(file)
    words = test_text.split(" ")

    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        else:
            word_count[word] += 1
    
    return word_count

    file.close()

result_test = print(word_count("test.txt"))

