from curl_cffi import requests

def isnotcolon(n,str):
    #print(n)
    #print(str[n])
    if str[n]=="\"":
        #print("是冒号")
        return 0
    else:
        #print("不是冒号")
        return 1

def checkstatus(str):
    test = requests.get(str)
    
    if test.status_code==404:
        print("无效文件")
        #print (test.status_code)
        #return 0
    elif test.status_code==200:
        print("有效文件：存储为")
        #print (test.status_code)
        #return 1
    else:
        print("错误")
        #return 0

def checkfile(str):
    test = requests.get(str)
    
    if test.status_code==404:
        #print("无效文件")
        #print (test.status_code)
        return 0
    elif test.status_code==200:
        #print("有效文件")
        #print (test.status_code)
        return 1
    else:
        #print("错误")
        return 0


url=input("请粘贴wiki语音记录网址，例如https://prts.wiki/w/麦哲伦/语音记录\n")
lan=int(input("输入语言选项：\n(1)日语voice\n(2)汉语voice_cn\n(3)韩语voice_kr\n(4)英语voice_en\n(5)特殊语言voice_custom\n"))
chname=input("输入生成文件的角色名称（不能有汉字）\n")

if 1<=lan<=5:
    print("收到")
else:
    print("错误")

response = requests.get(url)

find=response.text.find("data-voice-key")
key=find+16
#print(key)
#print(response.text[key])
#print(len(response.text))
num=0

if response.text[key-1]=="\"":
    print("成功定位")
    while isnotcolon(key+num,response.text):
        #print("开始放入")
        num=num+1
    print("名字长度是"+str(num))

sign=response.text[key:num+key]
print("角色代码为"+sign)

voicecode=""
if lan==1:
    voicecode="voice"
elif lan==2:
    voicecode="voice_cn"
elif lan==3:
    voicecode="voice_kr"
elif lan==4:
    voicecode="voice_en"
elif lan==5:
    voicecode="voice_custom"

filenum=1
#filenumset=[1000]
length = 100
# 生成固定长度的列表
filenumset = ["000" for _ in range(length)]
while filenum<=100:
    if 1<=filenum<=9:
        filenumset[filenum]="00"+str(filenum)
    elif 10<=filenum<=99:
        filenumset[filenum]="0"+str(filenum)
    filenum=filenum+1
#print (filenumset)

for i in range(1,100):
    filename="https://static.prts.wiki/"+voicecode+"/"+sign+"/CN_"+filenumset[i]+".wav"
    temp = requests.get(filename)
    #print (temp.status_code)
    checkstatus(filename)
    if checkfile(filename):
        output=chname+"-"+filenumset[i]+".wav"
        print(output)
        with open(output,'wb') as f:
            f.write(temp.content)
    #print(filename)