import nltk
from nltk import word_tokenize
from nltk import pos_tag

def recognize_dialog_acts(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    pos_tags = [tag for _, tag in tagged_words]

    if 'VB' in pos_tags:  
        return "Action"
    elif 'MD' in pos_tags:  
        return "Request/Suggestion"
    elif 'WP' in pos_tags:  
        return "Question"
    else:
        return "Statement"

if __name__ == "__main__":
    dialog = [
        "Could you please pass me the salt?",
        "I think we should go to the park.",
        "What time is the meeting?",
        "Bring the documents to my office."
    ]

    for sentence in dialog:
        dialog_act = recognize_dialog_acts(sentence)
        print(f"Dialog Act: {dialog_act} - Sentence: {sentence}")
