import itchat
import time
from itchat.content import *

switch = 'on' #自动回复开关
times = 0     #对同一用户的回复次数
toOldUserName = ''#记录当前对话用户（对方）

#根据系统时间获取本人当前所处状态
def getStat():
    stat = '' #本人所处状态
    localtime = time.localtime(time.time())  #获取当前系统时间
    hour = localtime.tm_hour    #获取当前小时
    wday = localtime.tm_wday    #获取当前星期，0为星期一
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

#自动回复函数
def sendByJarvis(toUserName):
    global switch
    global times
    global toOldUserName

    stat = getStat()

    if toOldUserName != toUserName:  #若最新接收到的消息不是来自当前对话用户，则将回复次数复位为0，记录为新对话
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

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])  #注册消息类型
def text_reply(msg):   #监听接收消息
    global times
    global toUserName
    global switch

    #若发信人为自己，根据接收的消息进行处理，若收到“1”，打开自动回复，若收到“0”，关闭自动回复
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

    #若发信人为其他用户，则又由Jarvis回复
    else:
        toUserName = msg['FromUserName']
        sendByJarvis(toUserName)

itchat.auto_login(hotReload=True)   #热登录，登录过一次之后再次打开程序时无需登录
itchat.run()
