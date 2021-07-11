import requests
import utils
import json

class Modem:

    retry = True

    def __init__(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)
        
        self.session = requests.Session()

        self.session.headers.update({
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'application/json, text/plain, */*',
            '_TclRequestVerificationKey' : 'KSDHSDFOGQ5WERYTUIQWERTYUISDFG1HJZXCVCXBN2GDSMNDHKVKFsVBNf',
            '_TclRequestVerificationToken': None,
            "Referer": self.config["url"]+"/index.html",
        })

    def loginRequest(self):
        loginResponse = self._jsonRequest("Login", {'UserName': utils.encrypt(self.config["username"]), 'Password':utils.encrypt(self.config["password"])})
        login = loginResponse["result"]
        token = utils.encrypt(str(login["token"]))
        self.session.headers.update({
            '_TclRequestVerificationToken': token
        })
        
    def _jsonRequest(self, method, params={}):
        #TODO: handle communication errors - requests.exceptions.ConnectionError
        resultObj = self.session.post(self.config["url"]+"/jrd/webapi", json={
            "id":"12",
            "jsonrpc":"2.0",
            "method":method,
            "params":params
        }).json()

        return resultObj

    def makeRequest(self, method, params={}):
        result = self._jsonRequest(method, params)
        if "error" in result:
            error = result["error"]
            if error["code"] in ('-32698', '-32699') and self.retry:
                self.loginRequest()
                # retry the call
                result = self._jsonRequest(method, params)
            else:
                raise Exception(error)

        return result["result"]