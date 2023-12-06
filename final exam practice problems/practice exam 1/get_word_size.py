def get_word_size(word) :
    if word == "" :
        return 0 
    else : 
        return 1 + get_word_size(word[:-1])
    
word = "rizzgyatt" # expected output : 9
print(get_word_size(word))

def process_sentence(sentence, process_word) :
    words = sentence.split()
    list = [process_word(word) for word in words]

    return list

sentence = 'the quick brown fox jumped over the lazy dog'
print(process_sentence(sentence, get_word_size)) # expected output [3,5,5,3,6,4,3,4,3]

