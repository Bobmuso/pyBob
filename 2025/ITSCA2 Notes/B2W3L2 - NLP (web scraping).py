

#Import Libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

#Send HTTP request
URL = 'https://realpython.github.io/fake-jobs/'
pageResponse = requests.get(URL)

if pageResponse.status_code == 200:
    pageContent = pageResponse.text
else:
    print(f'Failed to retrieve the page. Status Code: {pageResponse.status_code}')

#Parse the HTML
soup = BeautifulSoup(pageContent, 'html.parser')

#Find HTML element by ID
pageElementID = soup.find(id = 'ResultsContainer') #return 1st element under ID
pageElementID = soup.find_all(id = 'ResultsContainer') #return all elements under ID

#Find HTML element by class name
pageElementName = soup.find('div', class_ = 'card-content') #deduce to elements in 'card-content'
for eachElement in pageElementName:
    titleElement = eachElement.find('h2', class_ = 'title')
    companyElement = eachElement.find('h3', class_ = 'company')
    locationElement = eachElement.find('p', class_ = 'location')
    titleElement.text.strip() #Remove HTML components
    companyElement.text.strip()
    locationElement.text.strip()

#Find element by class name and text content (filter with keyword)
pageElementNameText = soup.find_all('h2', string = lambda text: 'python' in text.lower()) #filter for job ('h2') with python
len(pageElementNameText) # How many jobs/items found

for eachElement in pageElementNameText:
    print(eachElement.text.strip())

#Access parent elements
parentElementName = [h2Element.parent.parent.parent for h2Element in pageElementNameText]

#Import Libraries
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

#Send HTTP request
URL = "https://realpython.github.io/fake-jobs/"
pageResponse = requests.get(URL)

if pageResponse.status_code == 200:
    pageContent = pageResponse.text
    #print(pageContent)
else:
    print(f"Failed to retrieve the page. Status code: {pageResponse.status_code}")

soup = BeautifulSoup(pageContent, "html.parser")
#print(soup)

##
url = "https://www.imdb.com/title/tt0111161/reviews"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    pageContent = response.text
    soup = BeautifulSoup(pageContent, 'html.parser')
#    print(soup.prettify()[:1000])
    reviews = soup.find_all("div", class_="text show-more__control")
    reviewText = [eachReview.text.strip() for eachReview in reviews]
#    for review in reviewText:
#        print(review)

else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")

def getSentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def getWordFreq(text):
    blob = TextBlob(text)
    words = [words.lower() for words in blob.words if words.lower not in stopWords]
    wordFreq = blob.word_counts
    sortedWordFreq = sorted(wordFreq.items(), key = lambda item: item[1], reverse = True)
    mostCommonWordsFiltered = []
    for i in range(len(sortedWordFreq)):
        wordItem = sortedWordFreq[i]
        if not(wordItem[0] in stopWords):
            mostCommonWordsFiltered.append(wordItem)

    return mostCommonWordsFiltered



sentiments = [(eachReview, getSentiment(eachReview)) for eachReview in reviewText]

for eachReview, sentiments in sentiments:
    print(f'Review: {eachReview}\nSentiment Score: {sentiments}\n\n')

sentimentScores = [eachSentiment for _, eachSentiment in sentiments]
plt.figure(figsize = (10, 5))
sns.histplot(sentimentScores, bins = 30, color = 'blue')
plt.title('Distribution of Sentiment Score for "The Shawshank Redemption" Review')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.show()

allReviews = ' '.join(reviewText)
commonWords = getWordFreq(allReviews)
words, frequencies = zip(*commonWords)

plt.figure(figsize = (12, 6))
sns.barplot(x = list(frequencies), y = list(words))
plt.title('Top 20 Words most common words for "The Shawshank Redemption" reviews')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.show()

wordCloud = WordCloud(stopwords = stopWords, background_color = 'white').generate(allReviews)
plt.figure(figsize =(10, 5))
plt.imshow(wordCloud)
plt.axis('off')
plt.title('Word Cloud of "The Shawshank Redemption"')
plt.show()