import requests
import json

class CompareIt:
    _at = '' #accesstoken
    _endpoint = 'https://dev2.mittsmartahus.se/api/0/'
    _username = ''
    _password = ''

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def Login(self):
        uri = self._endpoint + 'user/login'
        postbody = {"username": self._username, "password": self._password}
        headers =  {"Content-Type":"application/json"}
        response = requests.post(uri, data=json.dumps(postbody), headers=headers)
        self._at = Util.setAccessToken(response.json()['at'])
        pass

    def GetAllEntities(self):
        uri = self._endpoint + 'view/overview'

        if len(self._at) > 1:
            headers =  {"Content-Type":"application/json", "Authorization": self._at}
            response = requests.get(uri, headers = headers)
        else:
            self.Login()
            return self.GetAllEntities(self)

        if response.status_code == 200:
            return response.json()
        else:
            return 'Error!'

    def GetEntity(self, uuid):
        uri = self._endpoint + 'object/'

        if len(self._at) > 1:
            headers =  {"Content-Type":"application/json", "Authorization": self._at}
            response = requests.get(uri, headers = headers)
        else:
            self.Login()
            return self.GetEntity(self, uuid)

        if response.status_code == 200:
            return response.json()
        else:
            return 'Error!'

    def SetEntity(self, uuid, value):
        pass

class Util:
    @staticmethod
    def parseSetValue(value):
        pass

    @staticmethod
    def setAccessToken(response):
        return 'Bearer ' + response