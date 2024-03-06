import nltk

from nltk import word_tokenize, pos_tag



# Example transformation-based tagger using a set of rules

class TransformationBasedTagger:

    def __init__(self, rules):

        self.rules = rules



    def tag(self, sentence):

        # Tokenize the sentence

        words = word_tokenize(sentence)



        # Initialize the tagged sentence with default tags

        tagged_sentence = pos_tag(words)



        # Apply transformation rules iteratively

        for rule in self.rules:

            tagged_sentence = self.apply_rule(tagged_sentence, rule)



        return tagged_sentence



    @staticmethod

    def apply_rule(tagged_sentence, rule):

        result = []



        for i in range(len(tagged_sentence)):

            word, tag = tagged_sentence[i]



            # Apply the rule if the word matches the pattern

            if nltk.re.search(rule[0], word) and tag != rule[1]:

                result.append((word, rule[1]))

            else:

                result.append((word, tag))



        return result



# Example transformation rules

transformation_rules = [

    (r'\bI\b', 'PRP'),

    (r'\bam\b', 'VBP'),

    (r'\bis\b', 'VBZ'),

    (r'\bare\b', 'VBP'),

    (r'\bwere\b', 'VBD'),

    # Add more rules as needed

]



# Example sentence

sentence = "I am going to the store."



# Create and use the transformation-based tagger

transformation_tagger = TransformationBasedTagger(transformation_rules)

tagged_sentence = transformation_tagger.tag(sentence)



# Display the result

print(tagged_sentence)
