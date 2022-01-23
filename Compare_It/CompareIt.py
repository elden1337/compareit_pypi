import requests

class CompareIt:
    _at = '' #accesstoken
    _endpoint = 'https://dev2.mittsmartahus.se/api/0/'
    _username = ''
    _password = ''

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def Login(self):
        print(self._username)
        pass

    def GetAllEntities(self):
        uri = self._endpoint + 'view/overview'

        headers =  {"Content-Type":"application/json", "Authorization": self._at}
        response = requests.get(uri, headers = headers)

        if response.status_code == 200:
            return response.json()
        else:
            return 'error'

    def GetEntity(self, uuid):
        pass

    def SetEntity(self, uuid, value):
        pass

class Util:
    @staticmethod
    def parseSetValue(value):
        pass

    @staticmethod
    def setAccessToken(response):
        at = 'hej'
        return 'Bearer ' + at