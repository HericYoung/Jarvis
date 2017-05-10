import itchat
import time
from itchat.content import *

switch = 'on'
times = 0
toOldUserName = ''

def getStat():
    stat = ''
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    wday = localtime.tm_wday
    if wday < 5:
        if (hour >= 9 and hour < 12) or (hour >= 12 and hour < 19):
            stat = 'working'
        elif hour < 13 and hour >=12:
            stat = 'lunch'
        elif hour < 7 and hour >= 23:
            stat = 'sleeping'
        else:
            stat = 'unknown'
    else:
        if hour < 8 and hour >= 23:
            stat = 'sleeping'
        else:
            stat = 'rest'
    return stat

def sendByJarvis(toUserName):
    global switch
    global times
    global toOldUserName

    stat = getStat()

    if toOldUserName != toUserName:
        toOldUserName = toUserName
        times = 0

    if switch == 'on':
        times = times + 1
        if times == 1:
            if stat == 'working':
                itchat.send("你好我是Jarvis，浩哥在上班，待会让他回复你|O_O|", toUserName)
            elif stat == 'lunch':
                itchat.send("你好我是Jarvis，浩哥去吃午饭了，待会让他回复你|O_O|", toUserName)
            elif stat == 'rest':
                itchat.send("你好我是Jarvis，浩哥今天放假，只是不知道现在在干嘛，待会让他回复你|O_O|", toUserName)
            elif stat == 'sleeping':
                itchat.send("你好我是Jarvis，浩哥在睡觉，等他醒了让他回复你|O_O|", toUserName)
            else:
                itchat.send("你好我是Jarvis，浩哥不知道去哪了，待会让他回复你|0_O|", toUserName)
            itchat.send("你才机器人|O_O|", toUserName)
        elif times < 3:
            itchat.send("好了知道了|O_O|", toUserName)
        elif times == 3:
            itchat.send("你不要为难一个机器人......|0_o|", toUserName)
        elif times == 4:
            itchat.send("不理你我要睡了|-.-|", toUserName)
        elif times > 4:
            itchat.send("|-_-|zzzZ...", toUserName)
    return

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    global times
    global toUserName
    global switch
    if msg['FromUserName'] == msg['ToUserName']:
        if msg['Content'] == "0":
            switch = 'off'
            times = 0
            itchat.send('自动回复已关闭',msg['ToUserName'])
        elif msg['Content'] == '1':
            switch = 'on'
            times = 0
            itchat.send('自动回复已打开', msg['ToUserName'])
        return
    else:
        toUserName = msg['FromUserName']
        sendByJarvis(toUserName)

itchat.auto_login(hotReload=True)
itchat.run()
