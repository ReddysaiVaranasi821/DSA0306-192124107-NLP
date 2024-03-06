import nltk

from nltk import word_tokenize



def stochastic_pos_tagger(text):



    words = word_tokenize(text)



    tagged_words = nltk.pos_tag(words)



    return tagged_words



sentence = "The cat is sitting on the mat."



tagged_sentence = stochastic_pos_tagger(sentence)



print(tagged_sentence)
