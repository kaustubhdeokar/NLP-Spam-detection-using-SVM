import os,sys
import string

#string.punctuations list 
table=str.maketrans('','',string.punctuation)

#super cool technique for removing the unwanted stuff...more written on the readme in the project.
def fault(i):
    return(i.translate(table))

#first for the spam objects
def spam():
    spamwords={}
    changedirectory=os.chdir("spam/")
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

#for genuine objects

def genuine():
    genuine={}
    changedirectory=os.chdir("C:\\Users\\Kaustubh\\Desktop\\nlp-project-kaustubh python3\\genuine/")
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

def test(spamwords,genuine):
    genuinecount=0
    spamcount=0
    os.chdir("C:\\Users\\Kaustubh\\Desktop\\nlp-project-kaustubh python3\\test/")
    testfolder=os.listdir(".")
    for i in testfolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in spamwords and k in genuine:
                    spamcount+=spamwords[k]
                    genuinecount+=genuine[k]
                elif k in spamwords:
                    spamcount+=spamwords[k]
                elif k in genuine:
                    genuinecount+=genuine[k]
                else:
                    print('Not both')
        print('file is:',str(i))
        print('spam count is:',spamcount)
        print('genuine count is:',genuinecount)
        if(spamcount>genuinecount):
            print('it is a spam')
            print('spam percent:',(spamcount/(spamcount+genuinecount))*100)
        else:
            print('it is genuine')
            print('genuine percent:',(genuinecount/(spamcount+genuinecount))*100)
        print()
        print()
        
if __name__=="__main__":
    """
    spamwords={}
    spamwords=spam()
    genuinewords={}
    genuinewords=genuine()
    test(spamwords,genuinewords)    
    """
    os.chdir("C:\\Users\\Kaustubh\\Desktop\\nlp-project-kaustubh python3/")
    f=open("spam.csv","r")
    counter=0
    for i in f:
        if(counter<2):
            print(i)
            counter+=1
        else:
            print('ok')
            break  
