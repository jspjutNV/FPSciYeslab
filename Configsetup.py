import shutil
import random

username = input("Username: ")
dpi = int(input("Mouse DPI: "))
sens = float(input("Custom sensitivity (deg/mm): "))
pri = bool(int(input("Which session first? 0-Custom, 1-Default: ")))

setting = "custom"
if pri: setting = "default"


userconfig = """{ 
    "settingsVersion": 1, 
    "users": [
        { 
            "id": "%s_custom", 
            "mouseDPI": %d, 
            "mouseDegPerMillimeter": %.2f
        }, 
        { 
            "id": "%s_default", 
            "mouseDPI": %d, 
            "mouseDegPerMillimeter": 1
        } ]
    
}""" % (username, dpi, sens, username, dpi)

sess = ["ssw", "ssg", "slw", "slg", "fsw", "fsg", "flw", "flg", "svsw"]

sess1 = []
sess2 = []

random.shuffle(sess)
sess1 += sess
random.shuffle(sess)
sess1 += sess

random.shuffle(sess)
sess2 += sess
random.shuffle(sess)
sess2 += sess

sess1 = ["prac"] + sess1
sess2 = ["prac"] + sess2

s1 = []
s2 = []
for e in sess1:
    s1.append(e)
    s1.append("calib")
for e in sess2:
    s2.append(e)
    s2.append("calib")

s1 = str(s1).replace("'", '"')
s2 = str(s2).replace("'", '"')

userstatus = """{ 
    "allowRepeat": true, 
    "currentUser": "%s_%s", 
    "sessions": [ "calib", "prac", "ssw", "ssg", "slw", "slg", "fsw", "fsg", "flw", "flg", "svsw" ], 
    "settingsVersion": 1, 
    "users": [ 
        { 
            "completedSessions": [ ], 
            "id": "%s_custom", 
            "sessions": %s
        }, 
        { 
            "completedSessions": [ ], 
            "id": "%s_default", 
            "sessions": %s
        } ]
    
}""" % (username, setting, username, s1, username, s2)

f = open("FPSci\\userconfig.Any", "w")
f.write(userconfig)
f.close()

f = open("FPSci\\userstatus.Any", "w")
f.write(userstatus)
f.close()
