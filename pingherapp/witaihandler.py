import solrhandler
from wit import Wit
import json
import os.path
from random import randint
BASE = os.path.dirname(os.path.abspath(__file__))
def converse(Query):
	access_token = "HUYFSZATE2FRGLETGVWWTCHNSVTXBKDC" 


	def send(request, response):
	    print(response['text'])
	actions = {
	    'send': send,    
	}
	tweet={"tweet_text":"","tweet_url":[],"media_url":[]}
	
	client = Wit(access_token=access_token, actions=actions)
	#Query=""
	data=client.converse(1,Query)
	X=""
	for key in data['entities'].keys():
	   	X=X+" "+str(data['entities'][key][0]['value'])
	mydict=json.load(open(os.path.join(BASE, "mydict.json")))
	solr=True
	for key_list in mydict.keys():
		flag=True
		for key in data['entities'].keys():
			if str(data['entities'][key][0]['value']).upper() not in str(key_list):
				flag=False
		if flag:
			if "JOKE" in key_list:
				x=randint(1,4)
				tweet['tweet_text']=mydict[key_list[:-1]+str(x)]
			else:
				tweet['tweet_text']=mydict[key_list]
			solr=False
	if len(data['entities'].keys())==0:
		solr=True
		X=Query
	if solr:
		tweet=solrhandler.solrcall(X,data)
	#print tweet['tweet_url'][0][0]
	x=[]
	for i in range(len(tweet['tweet_url'])):
		x.append(tweet['tweet_url'][i][0])
	tweet['tweet_url']=x
	print tweet
	return tweet

# whats your name
# what can you do
# What is your opinion on demonetization
# Tell me a joke
# Show me the most positive/neg/neut tweets <from dna> on demonetization
# Show me the most retweeted/favourited tweet <from dna> on demonetization
# Who implemented demonetization