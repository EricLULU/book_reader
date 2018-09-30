#import win32com.client
#import winsound
import pyttsx3

engine = pyttsx3.init()
print("开始设置")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)

print("开始读书，谢谢收听。")
engine.say("only english")
engine.say("开始读书，谢谢收听。")
engine.runAndWait()
engine.say("正在收听的是刘同的小说,《谁的青春不迷茫》")
engine.runAndWait()
with open(r"young.txt",'r') as f:
    for line in f.readlines():
        print(line)
        engine.say(line)
        engine.runAndWait()
        #speak.Speak(line)
engine.say("本书已经读完，谢谢！")

"""
speak.Speak("本书已经读完，谢谢！")
speak = win32com.client.Dispatch('SAPI.SPVOICE')

speak.Speak("开始语音读书")
print("开始读书，谢谢收听")
print("不想听的时候，可以直接关掉此窗口！")
print("正在收听的是刘同的小说,《谁的青春不迷茫》")
#winsound.Beep(2015, 3000)
with open(r"young.txt",'r') as f:
    for line in f.readlines():
        print(line)
        speak.Speak(line)
speak.Speak("本书已经读完，谢谢！")
"""
