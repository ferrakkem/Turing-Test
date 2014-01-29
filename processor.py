import random
import string
import copy
from knowledgeBase import *

puncChar = '?;:,!.@#$/\-+_*^><&()'
# checks if the character entered is a punctuation or not
def isPunc(char):
    if(puncChar.find(char) != -1):
        return True
    return False

# removes punctuation & redundant spaces
def cleanString(inputString):
    temp = ""
    prevChar = ""
    for char in inputString:
        if char.isspace() and prevChar.isspace():
            pass
        elif ((char.isspace() and not prevChar.isspace()) or not isPunc(char)):
            temp += char
            prevChar = char
        elif not prevChar.isspace() and isPunc(char):
            temp += ' '
            prevChar = ' '
    if temp.endswith(' '):
        temp = temp[0:-1]
    return temp
#
def processMessage(string):
	test=cleanString(string)
	global flag
	flag = True
	global ans
	ans = " "
	msg = test.split()
	#print msg
	#print len(Out)
	#print len(In)
	if not string:
		rnd=random.randint(0,len(Out[2])-1)
		ans=Out[2][rnd]
		return ans
	for i in range(len(In)):
		#print In[i]
		key=' '.join(In[i])
		key=key.split()
		#print key
		for j in range(len(key)):
			#print msg[j] + " " + key[j]
			if msg[j].lower()==key[j].lower():
				x=i
				flag=True
			else:
				flag=False
				break
		if flag:
			break
		#print "\n----------------\n"
	if flag:
		rnd=random.randint(0,len(Out[x])-1)
		ans=Out[x][rnd]
	else:
		rnd=random.randint(0,len(Out[4])-1)
		ans=Out[4][rnd]
	res=' '.join(msg[j+1:])
	#print res
	res=res.split()
	#print res
	#print len(res)
	for k in range(len(res)):
		#print "in"
		#print res[k]
		#print Ax[k]
		for l in range(len(Ax)):
			ver=' '.join(Ax[l])
			#print ver
			if res[k].lower()==ver.lower():
				#print ver
				ver2=' '.join(AxR[l])
				#print res[k]
				#print ver2
				res[k]=ver2
				#print res[k]
				break;
		#if res[k]==ver:
		#	print ver
	#ans=''.join(ans)+' '.join(res)
	val=ans.find('%')
	if val < 0:
		new = ''.join(ans)
	else:
		new=''.join(ans[:val])+' '.join(res)+''.join(ans[val+2:])
	#print new
	return ans
	
	
	
