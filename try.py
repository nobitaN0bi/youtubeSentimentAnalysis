from textblob import TextBlob

text = "I love this library. It's awesome."
blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
