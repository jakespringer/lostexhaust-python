import re

newline = re.compile("\\r")
tabs = re.compile("\\t")

class DataTxtImpl:
    contact = None
    households = None
    lookup = None
    persons = None
    relationships = None

    def __init__(self, contactPath, householdsPath, lookupPath, personsPath, relationshipsPath):
        self.contactPath = contactPath
        self.householdsPath = householdsPath
        self.lookupPath = lookupPath
        self.personsPath = personsPath
        self.relationshipsPath = relationshipsPath
        pass

    def getPerson(self, personId):
        if self.persons == None:
            with open(self.personsPath, "r") as f:
                self.persons = parseTxt(f.read())
        for i in range(0, len(self.persons)):
            if int(self.persons[i]["id"]) == personId:
                return self.persons[i]
        return None

    def getPersonIdsFromHousehold(self, householdId):
        if self.lookup == None:
            with open(self.lookupPath, "r") as f:
                self.lookup = parseTxt(f.read())
        ids = []
        for i in range(0, len(self.lookup)):
            if int(self.lookup[i]["household"]) == householdId:
                ids.append(int(self.lookup[i]["person"]))
        return ids

    def getHousehold(self, householdId):
        if self.households == None:
            with open(self.householdsPath, "r") as f:
                self.households = parseTxt(f.read())
        for i in range(0, len(self.households)):
            if int(self.households[i]["id"]) == householdId:
                return self.households[i]
        return None

    def getHouseholdIdsFromPerson(self, personId):
        if self.lookup == None:
            with open(self.lookupPath, "r") as f:
                self.lookup = parseTxt(f.read())
        ids = []
        for i in range(0, len(self.lookup)):
            if int(self.lookup[i]["person"]) == personId:
                ids.append(int(self.lookup[i]["household"]))
        return ids

    def getRelationships(self, personId):
        if self.relationships == None:
            with open(self.relationshipsPath, "r") as f:
                self.relationships = parseTxt(f.read())
        relationshipList = []
        for i in range(0, len(self.relationships)):
            if int(self.relationships[i]["id"]) == personId:
                relationshipList.append(self.relationships[i])
        return relationshipList

    def getContact(self, personId):
        if self.contact == None:
            with open(self.contactPath, "r") as f:
                self.contact = parseTxt(f.read())
        contactList = []
        for i in range(0, len(self.contact)):
            if int(self.contact[i]["id"]) == personId:
                contactList.append(self.contact[i])
        return contactList

def parseTxt(txt):
    lines = newline.split(txt)
    if len(lines) > 0:
        names = tabs.split(lines[0])
    else:
        return None
    parsedData = []
    for i in range(1, len(lines)):
        tokens = tabs.split(lines[i])
        if len(tokens) == len(names):
            parsedLine = dict()
            for j in range(0, len(tokens)):
                parsedLine[str(names[j])] = tokens[j]
            parsedData.append(parsedLine)
        elif len(tokens) != 1:
            return None
    return parsedData
