import nltk

from nltk import word_tokenize, pos_tag



def pos_tagging(text):

    

    words = word_tokenize(text)



    tagged_words = pos_tag(words)



    return tagged_words



text = "NLTK is a powerful library for natural language processing in Python."



tagged_text = pos_tagging(text)



print(tagged_text)
