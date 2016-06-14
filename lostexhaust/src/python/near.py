from templite import Templite
from os import path
import config
import math
import inject.inject

def lonLatDistance(originLatitude, originLongitude, targetLatitude, targetLongitude):
    lat = math.radians(originLatitude);
    lon = math.radians(originLongitude);
    lat2 = math.radians(targetLatitude);
    lon2 = math.radians(targetLongitude);
    deltaLat = lat2 - lat;
    deltaLon = lon2 - lon;
    sinPart = (math.sin(deltaLat / 2.0));
    cosPart = (math.cos(lat) * math.cos(lat2) * math.sin(deltaLon / 2.0));
    angle = 2.0 * math.asin(math.sqrt(sinPart * sinPart + cosPart * cosPart));
    return 3960.0 * angle;

def orderByDistance(origin, others, num):
    lat = float(origin["latitude"])
    lon = float(origin["longitude"])
    afterSorted = sorted(others, cmp=(lambda x, y: int(math.copysign(1, lonLatDistance(float(x["latitude"]), float(x["longitude"]), lat, lon) - lonLatDistance(float(y["latitude"]), float(y["longitude"]), lat, lon)))))
    afterSorted.remove(origin)
    return afterSorted[:min(num, len(afterSorted))]

def getPageNear():
    conf = config.loadConfig("../../conf/example_config.json")
    dataImpl = inject.inject.getDataImpl()
    sessionImpl = inject.inject.getSessionImpl()
    user = dataImpl.getPerson(1) # todo: change with sessionImpl.getSession(cookie).getId()
    user_households = map(lambda x: dataImpl.getHousehold(x), dataImpl.getHouseholdIdsFromPerson(1))
    user_household = user_households[0]
    households = dataImpl.getHouseholds()
    sorted_households = orderByDistance(user_household, households, 10)
    sorted_household_residents = []
    sorted_household_distances = []
    for i in range(0, len(sorted_households)):
        sorted_household_residents.append(map(lambda x: dataImpl.getPerson(x), dataImpl.getPersonIdsFromHousehold(int(sorted_households[i]["id"]))))
        sorted_household_distances.append("{0:.2f}".format(lonLatDistance(float(sorted_households[i]["latitude"]), float(sorted_households[i]["longitude"]), float(user_household["latitude"]), float(user_household["longitude"]))))
    carpools = []
    for i in range(0, len(sorted_households)):
        carpools.append((sorted_households[i], sorted_household_residents[i], sorted_household_distances[i]))
    t = Templite(filename=path.join(conf["projectRoot"], "src", "html", "near.templite"))
    return t.render(user=user, user_households=user_households, user_household_selected=0, carpools=carpools, num_results=10)

print(getPageNear())
