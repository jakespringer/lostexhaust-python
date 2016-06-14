from data_txt_impl import DataTxtImpl
from session_txt_impl import SessionTxtImpl

dataImpl = DataTxtImpl("../../res/example/contact.txt", "../../res/example/households.txt", "../../res/example/lookup.txt", "../../res/example/persons.txt", "../../res/example/relationships.txt")
sessionImpl = SessionTxtImpl()

def getDataImpl():
    return dataImpl

def getSessionImpl():
    return sessionImpl
