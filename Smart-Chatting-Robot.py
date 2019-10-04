#coding = utf-8
#by hollowman6

'''
说明：采用“图灵聊天机器人”API接口实现 
      http://www.turingapi.com/
    ***免责声明：该机器人所作出的任何回答都与本人观点无关！

instrution: Realized using the API from http://www.turingapi.com/
      Please using Chinese when chatting, also, for sure you can substitute it for other API 
    ***Note: The answers made by the Robot doesn't represent my own opinions!
'''

#载入相关库 Load related libraries
import requests

print("")
print("---图灵机器人智能聊天系统---")# ---Smart Chatting Robot---
print("")
name = input("请输入你的名字：")# Please enter your name:
print("")
print("好的，"+ name +"！现在开始聊天吧！O(∩_∩)O")# OK, xxx ! let's start chatting! O(∩_∩)O
print("输入'q'结束聊天······")# input 'q' to end the chat ......

#死循环 Infinite loop
while True:

    #忽略过程中的错误 Ignore errors during the process
    try:

        #API参数设置 Target API parameter setting
        url = "http://www.tuling123.com/openapi/api?key=1702c05fc1b94e2bb4de7fb2e61b21a3&info="
        print("")
        print(name + '：')
        question = input("    ")
        if question != 'q':
            answer = requests.get(url+question).text[23:-2]
            print("")
            print("机器人：")# Robot:
            print("    "+ answer)
        else:
            print("")
            print("正在退出中，请稍侯······")# Exiting, please wait ......
            break

    except Exception:
        print("    出错了，换个问题吧！o(*￣▽￣*)o")# Something went wrong, Let's change the question! o(*￣▽￣*)o

#程序结束 Ending