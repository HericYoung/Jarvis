#coding=utf8
import itchat
import time
from itchat.content import *

myId = "@24a57c8b088925c90098587ee7a204dd"
start = time.time()-100000
toUserName = 'noOne'

def sendByJarvis(toUserName):
    global start
    while time.time() < start + 10:
        print(start)
    else:
        itchat.send("'你好我是Jarvis，我大佬在上班，待会再让他回复你'",toUserName)


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def self_text(msg):
    global start
    global toUserName
    global myId
    if msg['FromUserName'] == myId:
        start = time.time() - 100000
        return
    if time.time() < start + 10:
        return
    toUserName = msg['FromUserName']
    start = time.time()
    sendByJarvis(toUserName)

itchat.auto_login(hotReload=True)
itchat.run()
