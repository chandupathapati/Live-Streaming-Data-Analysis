import json
import pandas as pd
import matplotlib.pyplot as plt


#I ran the Twitter_Streaming.py for 1 hour and collected data in below file for analysis
tweets_data_path ="C:\\Users\chandu\\PycharmProjects\\Twitter_Mining\\Data\\Live_Streaming_Data.JSON"

tweets_data = []
tweets_file = open(tweets_data_path, "r")


for line in tweets_file:
        try:
           tweet = json.loads(line)
           tweets_data.append(tweet)
           tweets = pd.DataFrame()
           tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
           tweets['language'] = map(lambda tweet: tweet['lang'], tweets_data)
           tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
        except:
           continue

#convert the map object to list for plotting
tweets_list_by_lang=list(tweets['language'][0])
tweets_by_lang_count=pd.value_counts(tweets_list_by_lang)[:5]

#plot the top 5 languages on the received tweets with filtered tags
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.set_xlabel('Languages', fontsize=7)
ax.set_ylabel('Number of tweets' , fontsize=7)
ax.set_title('Top 5 languages', fontsize=7, fontweight='bold')
tweets_by_lang_count.plot(ax=ax, kind='bar', color='green')
plt.show()

#convert the map object to list for plotting
tweets_list_by_Country=list(tweets['country'][0])
tweets_by_Country_count=pd.value_counts(tweets_list_by_Country)[:5]

#plot the top 5 countries on the received tweets with filtered tags
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.set_xlabel('Countries', fontsize=7)
ax.set_ylabel('Number of tweets' , fontsize=7)
ax.set_title('Top 5 countries', fontsize=7, fontweight='bold')
tweets_by_Country_count.plot(ax=ax, kind='bar', color='blue')
plt.show()
