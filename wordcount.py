"""Count words in file."""

def word_count(file):
    test_text = open(file)
    #words = test_text.split(' ')

    word_count = {}

    for line in test_text:
        lin = line.rstrip()
        line = lin.split(' ')
        #print(line)
        for words in line:
            words = words.split(' ')
            
            for word in words:

                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

#                   new_word_count= word_count + word_count[word]
    for word in word_count:
        print(word, word_count[word])         
    # return word_count


    # test_text.close()


   
    
    

word_count("test.txt")





