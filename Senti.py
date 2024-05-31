import concurrent.futures
from textblob import TextBlob

def analyze_sentiment(csv_file):
    # Read in the YouTube comments from the CSV file
    comments = []
    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comments.append(row['Comment'])

    # Function to calculate sentiment of a comment
    def calculate_sentiment(comment):
        lines = comment.split('\n')
        total_sentiment = sum(TextBlob(line).sentiment.polarity for line in lines)
        average_sentiment = total_sentiment / len(lines)
        if average_sentiment == 0.0:
            return 'neutral'
        elif average_sentiment > 0.0:
            return 'positive'
        else:
            return 'negative'

    # Use a ThreadPoolExecutor to calculate sentiment in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sentiments = list(executor.map(calculate_sentiment, comments))

    # Count the number of neutral, positive, and negative comments
    num_neutral = sentiments.count('neutral')
    num_positive = sentiments.count('positive')
    num_negative = sentiments.count('negative')

    # Return the results as a dictionary
    results = {'num_neutral': num_neutral, 'num_positive': num_positive, 'num_negative': num_negative}
    return results