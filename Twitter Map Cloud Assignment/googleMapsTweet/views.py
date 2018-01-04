import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse


keywords=['Food','Iphone','Tennis','Sports','Technology','Travel','World','Brand','Elections','Trump','trump', 'federer', 'nyu',
          'new york', '#ind', 'location', 'amazon', 'hugh', 'pizza', 'snapchat','instagram','facebook', 'bitcoin', 'violets', 'messi'
          ,'ronaldo', 'money', 'dan brown', 'apple', 'iphone X','iphone8','Google home mini', 'Googe', 'Apple watch', 'Macbook',
           'iphone', 'Trending', 'Me too', 'Alexa','elections','Chelsea', 'Man United', 'Nadal', 'ATP', 'ATP tour', 'BCCI', 'NASA',
           'ISRO', 'SRK', 'KRK','Bollywood','Hollywood']

def Index(Request):
    # redering base html page
    return render(Request, 'googleMapsTweet/base.html')

def Post(Request):
    # post request
    if Request.method == "POST":
        # Post request
        messages = Request.POST.get('Search', None)


        host = 'https://search-twittermapelasticsearch-g4ys5gux5wn5zzng2m3h552exe.us-east-1.es.amazonaws.com/tweetmap/tweet/_search?size=10000'\
               '&pretty=true&q=tweet:'

        def search(url, term):
            uri = url + term
            response = requests.get(uri)
            results = json.loads(response.text)
            #print(results)
            return results
        # verfying message
        if messages.lower() == 'food':
            l = 0
        elif messages.lower() == 'trump':
            l = 1
        elif messages.lower() == 'sports':
            l = 2
        elif messages.lower() == 'tennis':
            l = 3
        elif messages.lower() == 'technology':
            l = 4
        elif messages.lower() == 'elections':
            l = 5
        elif messages.lower() == 'iphone':
            l = 6
        elif messages.lower() == 'science':
            l = 7
        elif messages.lower() == 'world':
            l = 8
        elif messages.lower() == 'brand':
            l = 9
        # Store results by searching with given keywords
        results = search(host, keywords[l])
        # storing data from json data
        data = [res['_source']['coordinates'] for res in results['hits']['hits']]
        # storing tweet from json data
        tweet_data = [res['_source']['tweet'] for res in results['hits']['hits']]
        #fetching length of total records
        hits = len(data)
        # fetching length of hits
        length = {'hits': hits}
        coordinates = {}
        tweets = {}
        # Fetching coordinates and tweets from total hits object
        for i in range(hits):
            coordinates[i] = {'lat': data[i][1], 'lng': data[i][0]}
            tweets[i] = {'tweet': tweet_data[i]}
        # Returning Final Data
        data = {'coordinates': coordinates, 'length': length, 'tweets': tweets }
        return JsonResponse(data)