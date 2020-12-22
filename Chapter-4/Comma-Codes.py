def comma(listt):
    if len(listt)==0:
        return ""  #return empty string if empty list
    elif len(listt)==1:
        return str(listt[0])
    else:
        strr=str(listt[0])
        for i in range(1,len(listt)-1):
            strr+=', '+str(listt[i])
        strr+=', and '+str(listt[-1])
        return strr

spam = []

string=comma(spam)  #returns a string
print(string)