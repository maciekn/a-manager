import time
from modem import Modem

modem = Modem()


cells = ("NetworkName",
        "CellId",
        "RSSI",
        "RSRQ",
        "SINR",
        "RSRP",
        "LTE_state",
        "Band")
rowFormat = "{:<15} {:<15} {:<5} {:<5} {:<5} {:<5} {:<10} {:<3}"
print(rowFormat.format(*cells))
while True:
    dataFeed = modem.makeRequest("GetNetworkInfo")
    line = (dataFeed[c] for c in cells)
    print(rowFormat.format(*line))
    time.sleep(1)





    
