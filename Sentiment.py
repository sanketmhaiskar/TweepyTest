import codecs
class loaddata:
    global posDict
    global negDict
    def loadDictionary(self):
        global posDict,negDict
        temp = codecs.open("E:\Semester 1\SMM\pos.wn","r")
        posDict = set(temp.read().replace("_"," ").splitlines())
        temp = codecs.open("E:\Semester 1\SMM\\neg.wn","r")
        negDict = set(temp.read().replace("_"," ").splitlines())
        temp.close()
        return posDict,negDict

    def calculateSentiment(self,tweet):
        global posDict,negDict
        if(len(set(posDict).intersection(tweet)) > 0 ):
            return "Positive Tweet"
        elif(len(set(negDict).intersection(tweet)) >0):
            return "Negative Tweet"
        else:
            return "Cannot Classify"
