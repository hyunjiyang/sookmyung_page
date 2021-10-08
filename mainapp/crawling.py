import requests
import xmltodict
import time

def transportPrasing(busrouteid, stid, bus_ord):
    key = "vzA91Qq4LEFZCDiD2AxDLE7Q0crpj6R94w1Tl3huOFZIZVc%2FLy1fus68pmZSwv1z6N4hRwfG4QCSzV21eaF0fw%3D%3D"
    url = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey=" + key + "&stId="+stid + "&busRouteId=" + busrouteid + "&ord=" + bus_ord

    req = requests.get(url).content
    xmlObject = xmltodict.parse(req)
    allData = xmlObject['ServiceResult']['msgBody']['itemList']['arrmsg1']

    return allData