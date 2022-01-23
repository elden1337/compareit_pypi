import requests

class CompareIt:
    _at = '' #accesstoken
    _username = ''
    _password = ''

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def Login(self):
        print(self._username)
        pass

    def GetAllEntities(self):
        pass

    def GetEntity(self, uuid):
        pass

    def SetEntity(self, uuid, value):
        pass

class Util:
    @staticmethod
    def parseValue(value):
        pass