# https://www.nltk.org/


import nltk
import spacy

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")



text = """When we work with text, we can work with text units on different 
scales: we can work at the level of the document itself, such as a newspaper 
article; the paragraph, the sentence, or the word. Sentences are the main 
unit of processing in many NLP tasks. In this section, I will show you how 
to divide text into sentences.""".replace("\n", " ")

sentences = tokenizer.tokenize(text)
print(sentences)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    print(sentence)
    print(tokens)
    tagged = nltk.pos_tag(tokens)/Users/andy/ws/boutique/src/boutique/application_patterns/demo_nlp.py
    print(tagged[0:6])
    input()
