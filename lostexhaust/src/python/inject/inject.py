from data_catlin_impl import CatlinDataImpl

dataImpl = DataTxtImpl("../../../res/example/contact.txt", "../../../res/example/households.txt", "../../../res/example/lookup.txt", "../../../res/example/persons.txt", "../../../res/example/relationships.txt")

def getDataImpl():
    return dataImpl

def getSessionImpl():
    pass
