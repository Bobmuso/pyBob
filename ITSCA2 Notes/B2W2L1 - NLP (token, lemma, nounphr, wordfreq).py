from textblob import TextBlob, Word

#Tokenization (set of data broken down into sentences or words)
paragraph = """NLP enables computers and digital devices to recognize, understand and generate text and speech by 
combining computational linguistics—the rule-based modeling of human language—together with statistical modeling, 
machine learning and deep learning. 
NLP research has helped enable the era of generative AI, from the communication skills of large language models (LLMs) 
to the ability of image generation models to understand requests. NLP is already part of everyday life for many, 
powering search engines, prompting chatbots for customer service with spoken commands, voice-operated GPS systems and 
question-answering digital assistants on smartphones such as Amazon’s Alexa, Apple’s Siri and Microsoft’s Cortana. 
NLP also plays a growing role in enterprise solutions that help streamline and automate business operations, increase 
employee productivity and simplify business processes."""

blob = TextBlob(paragraph)
sentences = blob.sentences
words = blob.words

#Lemmatization (find base form of word e.g. feet = foot, drove = drive)
from textblob import TextBlob, Word
text = 'The striped are hanging on their feet for best'
blob = TextBlob(text)
originalWords = blob.words
lemmaWords = [Word(eachWord).lemmatize() for eachWord in originalWords]
userWord = input('Enter word to be lemmatized: ')
userPoS = input('Enter part of speech for each word (Noun: n, Verb: v, Adverb: r, Adjective: a): ')


def lemmaWithPoS(word, posTag):
    if posTag == 'a':
        return Word(word).lemmatize('a')
    elif posTag == 'v':
        return Word(word).lemmatize('v')
    elif posTag == 'n':
        return Word(word).lemmatize('n')
    elif posTag == 'r':
        return Word(word).lemmatize('r')
    else:
        return Word(word).lemmatize()

userWord = input('Enter word to be lemmatized: ').lower()
userPoS = input('Enter part of speech for each word (Noun: n, Verb: v, Adverb: r, Adjective: a): ')
lemmaWords = lemmaWithPoS(userWord, userPoS) #user lowercase

#Noun Phrase Extraction (adjective + its noun)
nounPhrases = blob.noun_phrases

#Word frequencies
from textblob import TextBlob
import string

userWords = input('Enter word to count:')
wordFreq = blob.word_counts[userWords]

#Activity

#lemmatize
blob = TextBlob(text)
tokens = blob.tokens #splits all words

lemmaWords = [Word.lemmatize() for word in tokens]

#Find word freq
word = [word.lower() for word in blob.words]
wordFreq = blob.word_counts
sortedWordFreq = sorted(wordFreq.items(), key = lambda item: item[1], reverse = True)
top20Words = sortedWordFreq[:20]
for word, freq in top20Words:
    print(f'{word}: {freq}')

#sentiment and polarity
sentiment = blob.sentiment
print(f'\nSentiment- Polarity: {sentiment.polarity}, subjectivity: {sentiment.subjectivity}')

