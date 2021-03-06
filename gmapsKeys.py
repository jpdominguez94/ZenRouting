__author__ = 'Justin'

from datetime import datetime

class keys:
    def __init__(self,keystringsfile,usagefile,datesfile, maxuses):
        self.keysdict = {}
        self.keysfilename = keystringsfile
        self.usagesfilename = usagefile
        self.datesfilename = datesfile
        self.maxusage = maxuses
        with open(keystringsfile) as f:
            keystrings = f.read().splitlines()
        with open(usagefile) as g:
            usages_ = g.read().splitlines()
        usages = []
        for use in usages_:
            usages.append(int(use))
        with open(datesfile) as h:
            dates = [tuple(map(int, i.split(','))) for i in h]
        for keystring,usage,date in zip(keystrings,usages,dates):
            self.keysdict[keystring] = key(keystring,usage,date)
    def updateKey(self,keystring,amount):
        currentkey = self.keysdict[keystring]
        now = datetime.now()
        currentdate = [now.day,now.month,now.year]
        if(currentkey.date == currentdate ):
            currentkey.usage += amount
        else:
            currentkey.usage = 0
            currentkey.date = currentdate
    def getKey(self):
        for keystring in self.keysdict:
            currentkey = self.keysdict[keystring]
            if(currentkey.usage < self.maxusage):
                return currentkey.name
    def printKeys(self):
        for keystring in self.keysdict:
            currentkey = self.keysdict[keystring]
            print('KeyName:',currentkey.name)
            print('KeyUsage:',currentkey.usage)
            print('KeyDate:',currentkey.date)
    def saveKeys(self):
        f = open(self.keysfilename,'w')
        g = open(self.usagesfilename,'w')
        h = open(self.datesfilename,'w')
        for keystring in self.keysdict:
            f.write(self.keysdict[keystring].name+'\n')
            g.write(str(self.keysdict[keystring].usage)+'\n')
            h.write(str(self.keysdict[keystring].date)[1:-1]+'\n')
        f.close()
        g.close()
        h.close()

class key:
    def __init__(self,string,pastuses,pastdate):
        now = datetime.now()
        self.name = string
        self.date = [now.day,now.month,now.year]
        if(pastdate != (now.day,now.month,now.year)):
            self.usage = 0
        else:
            self.usage = pastuses

