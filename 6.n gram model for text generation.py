Implement a basic N-gram model for text generation. For example, generate text using a bigram model using python.

PROGRAM :-

import random

def create_bigram_model(corpus):
    bigram_model = {}
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            if current_word in bigram_model:
                bigram_model[current_word].append(next_word)
            else:
                bigram_model[current_word] = [next_word]

    return bigram_model

def generate_text(bigram_model, start_word, length=10):
    generated_text = [start_word]
    current_word = start_word

    for _ in range(length - 1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

if __name__ == "__main__":
    
    corpus = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold."
    ]

    bigram_model = create_bigram_model(corpus)

    generated_text = generate_text(bigram_model, start_word="The", length=10)

    print("Generated Text:", generated_text)
