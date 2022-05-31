import requests
from requests.auth import HTTPDigestAuth

def findValueByKey(messeage, startKey, endKey, flip):
    lenKey = len(startKey)
    start = messeage.find(startKey)
    end = messeage.find(endKey)
    return messeage[start+lenKey+1: end-flip]

def parseM10V(ip):
    # M10V series:  HTTP Authentication is Digest Authentication
    url = "http://" + ip + "/command/inquiry.cgi?inqjs=camera"
    response = requests.get(url, auth=HTTPDigestAuth('admin', '9999'))
    content = response.text

    image_key_start = ['ImageSize1=', 'ImageSize2=', 'ImageSize3=']
    image_key_end = ['var FrameRate1', 'var FrameRate2', 'var FrameRate3']

    for i in range(len(image_key_start)):
        val = findValueByKey(content, image_key_start[i], image_key_end[i], 3)
        print("stream ", i, " = ", val)

def parseA51P(ip, user, pwd):
    url = "http://" + user + ":" + pwd + "@" + ip + "/ini.htm"
    response = requests.get(url)
    content = response.text

    image_key_start = ['streamname1', 'streamname2', 'streamname3']
    image_key_end = ['8557/h264', '8556/h264', '8555/mjpeg']

    for i in range(len(image_key_start)):
        val = findValueByKey(content, image_key_start[i], image_key_end[i], 21)
        print("stream ", i, " = ", val)

print("parse M10V ")
parseM10V("192.168.3.18")

print("parse A51P ")
parseA51P("192.168.3.51", "admin", "9999")





