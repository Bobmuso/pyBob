# Finding N-Grams (sequence of n items are extracted from a given text)
from textblob import TextBlob

text = "This is a simple text for generating n-grams with Textblob"
blob = TextBlob(text)
nGrams = blob.ngrams(3) #Create lists contain 3 words, each list removing prev word and adding next word from main text
for eachNGram in nGrams:
    print(f"{eachNGram}")

# Spell-checking
text = "I havv a spelg mistake in my sentense."
blob = TextBlob(text)
correctText = blob.correct()
print("Original Text:", text) # "Original Text: I havv a speling mistake in my sentense."
print("Corrected Text:", correctText) # "Corrected Text: I have a spelling mistake in my sentence."


for eachWord in blob.words:
    print(f"Word: {eachWord}, Spell Check: {eachWord.spellcheck()}")  # Check YT for error solution

#Language Translation
text = "Hello, how are you"
blob = TextBlob(text)
detectedLang = blob.detect_language()
translatedLang = blob.translate(to = 'es')
print(translatedLang)
translatedLang = blob.translate(to = 'fr')
print(translatedLang)


from googletrans import Translator

text = "Hello, how are you doing today. Did you have some coffee"
trans = Translator()
translatedFr = trans.translate(text, dest = 'fr')
print(translatedFr)
print(translatedFr.text)
print(translatedFr.src)

# user select language (dest)
def translateApp(text, targetLang):
    trans = Translator()
    translated = trans.translate(text, dest = targetLang)
    return translated.text

userText = input("Enter text for translation:")
userLang = input("Enter target language code (e.g. 'es' - spanish, 'fr' - French):")

transText = translateApp(userText, userLang)
print(f"Translated Text: {transText}")




# Sentiment Analysis
text = "TextBlob is a great for NLP. It makes text processing simple and fun!"
blob = Translator(text)
sentiment = blob.sentiment

print(f"Text: {text}")
print(f"Polarity: {sentiment.polarity}")
print(f"Subjectivity: {sentiment.subjectivity}")


#Language Translation
def translateApp(text, targetLang):
    trans = Translator()
    translated = trans.translate(text, dest = targetLang)
    return translated.text
    
def analyzeSentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment
    
userText = input("Enter text for translation:")
userLang = input("Enter target language code (e.g. 'es' - spanish, 'fr' - French):")

transText = translateApp(userText, userLang)
print(f"Translated Text: {transText}")

originalSentiment = analyzeSentiment(userText)
print(f"Original Text Sentiment: {originalSentiment}")

translatedSentiment = analyzeSentiment(transText)
print(f"Translated Text Sentiment - Polarity: {translatedSentiment.polarity}, Subjectivity: {translatedSentiment.subjectivity}")

