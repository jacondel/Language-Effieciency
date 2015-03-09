import requests
import codecs


def howFar(currentIndex,inputString):
    track=currentIndex+250
    if track>len(inputString):
        return len(inputString)
    while True:
        if inputString[track]==' ':
            return track

        track=track-1

def runWith(lang,files,shouldPrint):
    sol=[]
    for l in lang:
        for f in files:
            stringTrans=translate_spider(f[1],l)
            sol.append([stringTrans])
            if shouldPrint:
                stringsFile=str(f[0])+".out."+str(l)+".txt"
                countsFile="counts.txt"
                f1=codecs.open(stringsFile,'w','utf-8')
                f2=codecs.open(countsFile,'a')
                f1.write(stringTrans)
                f2.write(str(f[0])+ " "+str(l)+" characters: "+str(len(stringTrans))+ " words: "+ str(stringTrans.count(" "))+'\n')
    return sol


def translate_spider(string='default text', lg='fr'):
    inputString =string
    targetLanguage=lg
    solutionString=""
    currentIndex=0

    while currentIndex<len(inputString):
        endingIndex=howFar(currentIndex,inputString)
        shortenedString=inputString[currentIndex:endingIndex]
        shortenedString=shortenedString.rstrip('\n')
        url ="http://www.google.com/translate_t?langpair=en|"+targetLanguage+"&text="+shortenedString
        r=requests.get(url)
        html=str(r.text)
        result=extract(html)
        solutionString=solutionString+result + " "
        currentIndex=endingIndex+1
    return solutionString
def extract(s):
    location = s.find("long_text")
    if location == -1:
        location = s.index("short_text")
    for i in range(0,len(s)):
        if s[location -i] == "<":
            left=location-i
            break

    exitCount=0
    openCount=0
    result=""
    for i in range(left ,len(s)):
        if s[i] == "<": #which the first one will
            openCount=openCount+1
            if s[i+1] == "/":
                exitCount=exitCount-1
            else:
                exitCount=exitCount+1
            continue
        if s[i] == ">":
            openCount=openCount-1
            continue
        if exitCount==0:
            break
        if openCount==0: #inside brackets
            result=result+s[i]


    rep = {"&#39":"\'"  , "â":"-"  , "&quot;":"\""    ,    "';":"\'"  ,   ";'":"\'" }
    for key in rep:
        result=result.replace(key,rep[key])
    #result=result.replace("&#39","'")

    return result







languages = ['en','fr', 'it', 'ru']
names = ["Encodings.txt","Thoreau.txt"]

files=[]
for x in names:
    files.append([x,open(x).read()]) #files[0] is name files[1] is string
solution=runWith(languages,files,True)










