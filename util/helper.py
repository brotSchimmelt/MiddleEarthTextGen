import re


def remove_spaces(s):
    
    # replaces multiple whitespaces with a single space
    x =  re.sub(' +', ' ', s.replace('\t', ' '))
    return x.replace(' \n ', '\n')
