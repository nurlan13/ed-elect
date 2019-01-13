#!/usr/bin/env python3


# Run this search directly from the command line. Input format:
# ./term_scraper.py "[search term]" "[start data--format: YYYY-MM-DD]"
# Put quotation marks around both those inputs
# Example input:
# ./term_scraper.py "#potentialgrizzlies" "2019-01-01"

#Results print to term_search_results folder



import tweepy
import csv
import argparse

parser=argparse.ArgumentParser(description="scrape Twitter for terms")
parser.add_argument("search_term")
parser.add_argument("start_date")
args=parser.parse_args()

search_for=args.search_term
start_date=args.start_date

consumer_key="jJevgPoZqCvvlaEaDfCjSo3T4"
consumer_secret="s5uGQVieitvw5CT5FVBj7yM08aP84zf8HNpm4Ya99RtxsTnBA2"

access_token="1083483578359599104-iesJJeVOjPKmTB4peDWVIWzIJCl0rU"
access_token_secret="QREgbBttdMhWRCE7xBtXAIzNN0tG65QsvIstMxmgjcrt3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_name= "term_search_results/results_for_" + search_for + ".csv"

with open(file_name, 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	#Iterate through all Tweets:
#	poli_tweets=[1,2]
#	while len(poli_tweets) > 0:
	poli_tweets = tweepy.Cursor(api.search,q=search_for, count = 100, tweet_mode="extended", since=start_date).items()
	for tweet in poli_tweets:
		csvwriter.writerow([tweet.user.name]+[tweet.user.location]+[tweet.user.verified]+[tweet.id]+[tweet.created_at]+[tweet.full_text]+[tweet.place]+[tweet.retweet_count]+[tweet.favorite_count])