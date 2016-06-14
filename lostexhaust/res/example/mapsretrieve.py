from gmaps import Geocoding
from gmaps import errors
import sys

geo = Geocoding(api_key="AIzaSyCAU19MydrGYH5TulC8jFS9EYv8EiYLegY")

address = "".join(sys.argv[1:])
place = geo.geocode(address)[0]
print(place["place_id"] + "\t" + str(place["geometry"]["location"]["lat"]) + "\t" + str(place["geometry"]["location"]["lng"]))
