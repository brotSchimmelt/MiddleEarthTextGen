import re


def remove_spaces(s):    
    # replaces multiple whitespaces with a single space
    return re.sub(' +', ' ', s.replace('\t', ' ')).replace(' \n ', '\n')


def remove_spaces_concisely(s):
    # convert every pdf page to a single line in the output
    return re.sub('\s+', ' ', s).replace(' \n', '\n')
