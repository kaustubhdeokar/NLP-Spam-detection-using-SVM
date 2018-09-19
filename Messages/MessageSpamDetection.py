import os
import time
import string
import pandas as pd

#string.punctuations list 
table=str.maketrans('','',string.punctuation)
#
def fault(i):
    return(i.translate(table))

#first for the spam objects
def spam(path):
    os.chdir(path)
    spamwords={}
    changedirectory=os.chdir("Spam/")
    spamfolder=os.listdir(".")
    for i in spamfolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in spamwords:
                    spamwords[k]=spamwords[k]+1
                else:
                    spamwords[k]=1
    return spamwords

def genuine(path):
    os.chdir(path)
    genuine={}
    changedirectory=os.chdir("Ham/")
    genuinefolder=os.listdir(".")
    for i in genuinefolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in genuine:
                    genuine[k]=genuine[k]+1
                else:
                    genuine[k]=1
    return genuine

def test(spamwords,genuine,path):
    os.chdir(path)
    genuinecount=0
    spamcount=0
    os.chdir("SpamDirTest")
    testfolder=os.listdir(".")
    for i in testfolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in spamwords and k in genuine:
                    spamcount+=1
                    genuinecount+=1
                elif k in spamwords:
                    spamcount+=1
                elif k in genuine:
                    genuinecount+=1

        print('file is:',str(i))
        print('spam count is:',spamcount)
        print('genuine count is:',genuinecount)
        print("Deciding the K:")
        k=40
        spampercent=(spamcount/(spamcount+genuinecount))*100
        genuinepercent=100-spampercent
        if(spampercent>k):
            print('it is a spam')
            print('spam percent:',spampercent)
        else:
            print('it is genuine')
            print('genuine percent:',genuinepercent)
        print()
        print()
        

if __name__=="__main__":
    counter=0
    t=time.time()
    path2=os.getcwd()
    f=open("spamandham.csv","r+")
    os.mkdir("SpamDir")
    os.chdir("SpamDir")
    path=os.getcwd()
    for i in f:
        if(counter>0 and counter<500):
            counter+=1
            if(i[0]=='s'):
                if not os.path.exists("Spam"):
                    os.mkdir("Spam")
                os.chdir("Spam")
                f=open("spam"+str(counter),"w+")
                newcounter=0
                for j in i:
                    if(newcounter>4):
                        f.write(j)
                    else:
                        newcounter+=1
                f.close()
                os.chdir(path)
            else:
                if not os.path.exists("Ham"):
                    os.mkdir("Ham")
                os.chdir("Ham")
                f=open("ham"+str(counter),"w+")
                newcounter=0
                for j in i:
                    if(newcounter>4):
                        f.write(j)
                    else:
                        newcounter+=1
                f.close()
                os.chdir(path)           
        else:
            counter+=1
    spamwords={}
    spamwords=spam(path)
    genuinewords={}
    genuinewords=genuine(path)
    test(spamwords,genuinewords,path2)
    
    
    
        
