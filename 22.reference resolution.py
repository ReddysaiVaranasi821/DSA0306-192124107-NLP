def resolve_references(text):
    entities = {}  

    sentences = text.split('. ')  

    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 1):
            if words[i].lower() in ['he', 'she', 'it'] and words[i + 1].lower() not in ['he', 'she', 'it']:
                
                entities[words[i].lower()] = words[i + 1]

    for pronoun, entity in entities.items():
        print(f"Resolved: {pronoun} -> {entity}")

if __name__ == "__main__":
    input_text = """
    John went to the store. He bought some groceries.
    Mary likes to read books. She borrowed one from the library.
    The cat was sleeping. It woke up and stretched.
    """

    resolve_references(input_text)
