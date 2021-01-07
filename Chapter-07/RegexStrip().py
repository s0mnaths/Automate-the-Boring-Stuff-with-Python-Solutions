import re

def regexStrip(string, CharsToRemove=None):
    if CharsToRemove==None:
        subREgex=re.compile(r'(^ *)|( *$)')
        return subREgex.sub('',string)
    else:
        regexEscapeChars = ['*', '{', '}', '[', ']', '(', ')', '^', '$', '.', '+', '?', '|']
        if(CharsToRemove in regexEscapeChars):
            CharsToRemove='\\'+CharsToRemove
        subREgex=re.compile('^'+CharsToRemove+'*|'+CharsToRemove+'*$')
        return subREgex.sub('',string)