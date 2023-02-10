import requests, json, os
from elasticsearch import Elasticsearch 

es = Elasticsearch('http://localhost:9200')


category_id = {
    "1": "Film & Animation",
    "2": "Autos & Vehicles",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "18": "Short Movies",
    "19": "Travel & Events",
    "20": "Gaming",
    "21": "Videoblogging",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology",
    "29": "Nonprofits & Activism",
    "30": "Movies",
    "31": "Anime/Animation",
    "32": "Action/Adventure",
    "33": "Classics",
    "34": "Comedy",
    "35": "Documentary",
    "36": "Drama",
    "37": "Family",
    "38": "Foreign",
    "39": "Horror",
    "40": "Sci-Fi/Fantasy",
    "41": "Thriller",
    "42": "Shorts",
    "43": "Shows",
    "44": "Trailers"
}

f = open("output.json") #set filename in later
docket_content = f.read()

# Send the data into es
Bbody=json.loads(docket_content)
response = es.index(index='myindex', ignore=400, body = Bbody)
print(len(response))


my_body = {
    "size": 0,
    "aggs": {
        "my_agg_name": {
            "terms": {
                "size": 100,
                "snippet" : {"categoryId"}
            }
        }
    }
}

body = {
	#"from": 10,            # get docs from the number 10
    #"size": 100,           # get 100 docs (default = 10)
    "fields": ["kind", "etag", "id", "snippet"],   # get only wanted fields
	 #"query": {            # the query
        
	 #},        
    "sort": {            # to sort
        "snippet.categoryId": {
            
                "order": "desc"
            
        }
    }
}

r = es.search(index='myindex', body=body)
print(r)















