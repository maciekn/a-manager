import time
import json
import requests


def loadConfig():
    with open("config.json", "r") as f:
        return json.load(f)

config = loadConfig()

"""
Derived from original JS function:
  s.encrypt = function (e) {
    if ('' == e || void 0 == e) return '';
    for (var t = 'e5dl12XYVggihggafXWf0f2YSf2Xngd1', a = [
    ], i = '', s = 0; s < e.length; s++) {
      var n = e.charAt(s),
      r = n.charCodeAt();
      a[2 * s] = 240 & t[s % t.length].charCodeAt() | 15 & r ^ 15 & t[s % t.length].charCodeAt(),
      a[2 * s + 1] = 240 & t[s % t.length].charCodeAt() | r >> 4 ^ 15 & t[s % t.length].charCodeAt()
    }
    for (var s = 0; s < a.length; s++) i += String.fromCharCode(a[s]);
    return i
"""
def encrypt(content):
    keyTable = "e5dl12XYVggihggafXWf0f2YSf2Xngd1"
    keyTableLength = len(keyTable)

    if(len(content) == 0):
        return ""

    result = ""
    
    for i in range(len(content)):
        inputCharacter = ord(content[i])
        outputByte = ord(keyTable[i % keyTableLength])
        firstChar = 240 & outputByte | 15 & inputCharacter ^ 15 & outputByte
        result += chr(firstChar)
        secondChar = 240 & outputByte | inputCharacter >> 4 ^ 15 & outputByte
        result += chr(secondChar)

    return result


with requests.Session() as session:
    session.headers.update({
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'application/json, text/plain, */*',
        '_TclRequestVerificationKey' : 'KSDHSDFOGQ5WERYTUIQWERTYUISDFG1HJZXCVCXBN2GDSMNDHKVKFsVBNf',
        '_TclRequestVerificationToken': None,
        "Referer": config["url"]+"/index.html",
    })

    def jsonRequest(method, params={}):
        resultObj = session.post(config["url"]+"/jrd/webapi", json={
            "id":"12",
            "jsonrpc":"2.0",
            "method":method,
            "params":params
        }).json()
        if "error" in resultObj:
            error = resultObj["error"]
            if error["code"] in ('-32698', '-32699'):
                loginRequest()
                # retry the call
                return jsonRequest(method, params)
            else:
                raise Exception(error)

        return resultObj["result"]

    def loginRequest():
        loginResponse = jsonRequest("Login", {'UserName': encrypt(config["username"]), 'Password':encrypt(config["password"])})
        token = encrypt(str(loginResponse["token"]))
        session.headers.update({
            '_TclRequestVerificationToken': token
        })

    
    cells = ("NetworkName",
            "CellId",
            "RSSI",
            "SINR",
            "RSRP",
            "LTE_state",
            "Band")
    rowFormat = "{:<15} {:<15} {:<5} {:<5} {:<5} {:<10} {:<3}"
    print(rowFormat.format(*cells))
    while True:
        dataFeed = jsonRequest("GetNetworkInfo")
        line = (dataFeed[c] for c in cells)
        print(rowFormat.format(*line))
        time.sleep(1)





    
