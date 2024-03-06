import nltk

from nltk import word_tokenize, pos_tag

from nltk.tokenize import RegexpTokenizer



# Example rule-based part-of-speech tagging system using regular expressions

class RuleBasedPosTagger:

    def __init__(self):

        # Define regular expression patterns for common part-of-speech categories

        self.patterns = [

            (r'\b(?:he|she|it|they)\b', 'PRP'),  # Personal pronouns

            (r'\b(?:is|am|are|was|were)\b', 'VBP'),  # Verbs (present tense)

            (r'\b(?:I|you|he|she|it|we|they)\b', 'PRP'),  # Personal pronouns

            (r'\b(?:a|an|the)\b', 'DT'),  # Determiners

            (r'\b(?:\d+)\b', 'CD'),  # Cardinal numbers

            (r'\b(?:\w+\'\w+)\b', 'POS'),  # Possessive nouns

            (r'\b(?:\w+ing)\b', 'VBG'),  # Gerunds

            (r'\b(?:\w+ed)\b', 'VBD'),  # Past tense verbs

            (r'\b(?:\w+ly)\b', 'RB'),  # Adverbs

            (r'\b(?:\w+s)\b', 'NNS'),  # Plural nouns

            (r'\b(?:\w+\'s)\b', 'POS'),  # Possessive nouns

            (r'\b(?:\w+)\b', 'NN'),  # Default to nouns

        ]



        # Create a regex-based tokenizer

        self.tokenizer = RegexpTokenizer(r'\w+|\$[\d\.]+|\S+')



    def tag(self, text):

        # Tokenize the text

        words = self.tokenizer.tokenize(text)



        # Apply the regular expression patterns for part-of-speech tagging

        tagged_words = [(word, tag) if isinstance(pattern, str) else (word, tag) for pattern, tag in self.patterns for word in words if nltk.re.search(pattern, word)]



        return tagged_words



# Example text

text = "She is reading a book on natural language processing."



# Create and use the rule-based part-of-speech tagger

rule_based_tagger = RuleBasedPosTagger()

tagged_text = rule_based_tagger.tag(text)



# Display the result

print(tagged_text)
