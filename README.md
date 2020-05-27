# travel_time.py
This is a small script that returns travel times to multiple destinations from multiple sources using the Google Distance Matrix API. I made this because I couldn't really find anything that allows you to find travel times via Google Maps in bulk operations. This essentially just acts as an accessor to the Distance matrix API via the python client and formats it the way I want to view it. Originally made this to easily find parks to visit because I am throroughly perturbed by the embedded map GUIs in many parks websites.

## Requirements/Installation
* Obtain a Google Cloud API Key for the [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/get-api-key)
* [googlemaps Python client library](https://github.com/googlemaps/google-maps-services-python): pip install googlemaps

## How To Use
python travel_time.py -k [API KEY] -s [source locations input file] -d [destination locations input file]

* specify the API key
* specify the input files for sources and destinations
* -sbt is an optional boolean flag to sort results by travel time
* There are optional arguments that can be provided that match up with the optional request params (see appendix below)

### Example
python travel_time.py -k NotARealAPIKey -s sources.txt -d dests.txt -sbt

Example Output:
```
Configurations
{'arrival_time': None,
 'avoid': None,
 'departure_time': None,
 'language': None,
 'mode': None,
 'region': None,
 'traffic_model': None,
 'transit_mode': None,
 'transit_routing_preference': None,
 'units': None}

From: Seattle, WA, USA
Discovery Park, 3801 Discovery Park Blvd, Seattle, WA 98199, USA - 19 mins
Olympic National Park, 3002 Mt Angeles Rd, Port Angeles, WA 98362, USA - 2 hours 48 mins
Houston, TX, USA - 1 day 11 hours
Ellis Island, United States - 1 day 18 hours

From: Topeka, KS, USA
Houston, TX, USA - 10 hours 43 mins
Ellis Island, United States - 19 hours 11 mins
Discovery Park, 3801 Discovery Park Blvd, Seattle, WA 98199, USA - 1 day 4 hours
Olympic National Park, 3002 Mt Angeles Rd, Port Angeles, WA 98362, USA - 1 day 5 hours

From: Holy Boulders, Shawnee National Forest, 1975 Hutchins Creek Rd, Alto Pass, IL 62905, USA
Houston, TX, USA - 11 hours 45 mins
Ellis Island, United States - 15 hours 29 mins
Discovery Park, 3801 Discovery Park Blvd, Seattle, WA 98199, USA - 1 day 9 hours
Olympic National Park, 3002 Mt Angeles Rd, Port Angeles, WA 98362, USA - 1 day 12 hours
```

### Appendix
Info on optional request params or how the distance matrix is formatted
* [Python client library class](https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/distance_matrix.py)
* [Google Distance Matrix API documentation](https://developers.google.com/maps/documentation/distance-matrix/intro#DistanceMatrixRequests)

