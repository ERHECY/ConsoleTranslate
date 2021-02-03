import requests
import json
import os

def youdaoapi(text,debug):
    text = text.replace(' ','%20').replace('\'','').replace('\"','')
    if (debug == 1):
        print("输入文字转换后："+text)
    url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i='+text
    re = requests.get(url)
    trjson = json.loads(re.text)
    ada = (str)(trjson['translateResult'])
    ada = ada.replace('[[','').replace(']]','').replace('},{','}|{').replace('}, {','}|{')
    trlist = (list)(ada.split('|'))
    b =''
    for ta in range(len(trlist)):
        tr = (str)(trlist[ta]).replace('\'','\"')
        if(debug == 0):
            a = json.loads(tr)
            b += a['tgt']
        else:
            b += tr
    return b

if __name__ == '__main__':
    print("开始翻译请输入:")
    debug = 0
    while (True):
        text = input()
        if(text == '--help'):
            print("直接输入文本自动进行翻译\n命令列表\n--clear 清空记录\n--exit 退出程序\n--debug 测试模式")
        elif(text == '--clear'):
            os.system('cls')
        elif(text == '--exit'):
            exit(1)
        elif(text == '--debug'):
            if (debug == 0):
                debug = 1
                print("测试模式已启用")
            else:
                debug = 0
                print("测试模式已关闭")
        elif(text == ''):
            print("请输入要翻译的文本，或者输入--help显示帮助")
        else:
            print(youdaoapi(text, debug) + '\n')
