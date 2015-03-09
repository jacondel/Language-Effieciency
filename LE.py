import requests
from bs4 import BeautifulSoup


def howFar(currentIndex,inputString):
    track=currentIndex+250
    if track>len(inputString):
        return len(inputString)
    while True:
        if inputString[track]==' ':
            return track

        track=track-1


    #r=requests.get('http://translate.reference.com/translate?query=that%20chicken&src=en&dst=fr')

def runWith(lang,files,shouldPrint):
    sol=[]
    for l in lang:
        for f in files:
            stringTrans=translate_spider(f[1],l)
            sol.append([stringTrans])
            if shouldPrint:
                print(f[0], " ", l," characters: ",len(stringTrans), " words: ", stringTrans.count(" ") )
                print(stringTrans)
    return sol


def translate_spider(string='default text', lg='fr'):
    inputString =string
    targetLanguage=lg
    solutionString=""
    currentIndex=0

    #url ="http://www.google.com/translate_t?langpair=en|es&text=Hello, world it is good!"
    while currentIndex<len(inputString):
        #print("running",targetLanguage, currentIndex,"of",len(inputString))
        endingIndex=howFar(currentIndex,inputString)
        #print("how far:", endingIndex)
        shortenedString=inputString[currentIndex:endingIndex]
        shortenedString=shortenedString.rstrip('\n')
        #print("shortened String: ",shortenedString)
        url ="http://www.google.com/translate_t?langpair=en|"+targetLanguage+"&text="+shortenedString
        #print("url: ",url)

        #############
        r=requests.get(url)
        html=str(r.text)
        #print(html)
        result=extract(html)


        #soup = BeautifulSoup(r.text)
        #print(soup)
        #links = soup.find_all('span' , {'class': 'long_text'})
        #print(links.__len__())
        #if links.__len__() ==0:
        #    links = soup.find_all("span","short_text")
        #result=""
        #for x in links:
        #    print("inside foreach with x= ", str(x))
        #    result=x.string
        #   # result=extract(str(x))
        #    print("result: ",result)
        #############
      #

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
names = ["Encodings.txt"]

files=[]
for x in names:
    files.append([x,open(x).read()]) #files[0] is name files[1] is string
solution=runWith(languages,files,True)










