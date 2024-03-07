import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple Inc. is a technology company based in Cupertino, California. Tim Cook is the CEO."
doc = nlp(text)
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
organization_entities = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
print("Organizations:", organization_entities)
