import requests
import json

class CompareIt:
    _at = ''
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
        return self.__GetInternal(uri)

    def GetEntity(self, uuid):
        uri = self._endpoint + 'object/' + uuid
        return self.__GetInternal(uri)

    def __GetInternal(self, uri):
        if len(self._at) > 1:
            headers =  {"Content-Type":"application/json", "Authorization": self._at}
            response = requests.get(uri, headers = headers)
        else:
            self.Login()
            return self.__GetInternal(uri)

        if response.status_code == 200:
            return json.dumps(response.json())
        else:
            return 'Error!'

    def SetEntity(self, uuid, value):

        # if(uuentity.type == EntityType.Dimable)
        #     {
        #         if (value.ToLower() == "on")
        #         {
        #             value = "100";
        #         }
        #         else if (value.ToLower() == "off")
        #         {
        #             value = "0";
        #         }
        #     }
        #     else if (uuentity.type == EntityType.Binary)
        #     {
        #         if (value.ToLower() == "on")
        #         {
        #             value = "True";
        #         }
        #         else if (value.ToLower() == "off")
        #         {
        #             value = "False";
        #         }
        #     }

        #     var obj = new UpdateObject(value, uuentity.type, dim);
        #     var data = JsonConvert.SerializeObject(obj);

        #     var request = new RestRequest("object/" + uuentity.uuid, Method.PUT);
        #     request.RequestFormat = DataFormat.Json;
        #     request.AddHeader("Authorization", _accessToken == string.Empty ? Login() : _accessToken);
        #     IRestResponse response = null;

        #     request.AddJsonBody(data);
        #     response = _client.Execute(request);
        #     return response.Content;

        pass

class Util:
    @staticmethod
    def parseSetValue(value):
        pass

    @staticmethod
    def setAccessToken(response):
        return 'Bearer ' + response