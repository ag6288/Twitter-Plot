# Twitter-Plot
Web application collects Tweets and represents the Tweets on GoogleMaps. Following are the required steps:  

1. Twitter Streaming API is used to fetch tweets from the twitter hose in real-time.
2. AWS ElasticSearch to store the tweets on the back-end.
3. Google Maps API is used to render these filtered tweets on the map.
4. Application is deployed on AWS Elastic Beanstalk in an auto-scaling environment.
5. AWS ElasticSearch’s geospatial feature that shows tweets within a certain distance from the point the user clicks on the map. 
