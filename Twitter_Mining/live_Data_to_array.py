import json


tweets_data_path ="C:\\Users\chandu\\PycharmProjects\\chandra_Mining\\Data\\twitter_Data.txt"

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(tweets_data)
print(len(tweets_data))
