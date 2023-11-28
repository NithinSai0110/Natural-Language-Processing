import spacy
nlp = spacy.load("en_core_web_sm")
sentences = [
    "The cat sat on the mat.",
    "She quickly ran to catch the bus."
]
for sentence in sentences:
    doc = nlp(sentence)
    print("\nDependency Parsing for Sentence:")
    print(sentence)
    for token in doc:
        print(f"{token.text} --{token.dep_}--> {token.head.text}")
