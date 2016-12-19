import re
import string

def clean_text(text):
    # get rid of links
    url_pattern = u'((http|ftp|https):\/\/)?[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
    text = [re.sub(url_pattern, ' ', x) for x in text]

    # make sure there are spaces between emojis
    regex = re.compile(ur'([\u263a-\U0001f645])')
    text = [regex.sub(ur' \1 ', item) for item in text]

    # get rid of newline characters
    text = [re.sub('[\s+]', ' ', x) for x in text]

    # get rid of numbers that are surroudned by spaces
    text = [re.sub("\s+[\d]", " <NUMERIC> ", x) for x in text]

    emot = {'EMOT01': '\:\)', 
        'EMOT02': '\:\(*',
        'EMOT03': '\:P', 
        'EMOT04': '\:\/', 
        'EMOT05':"\:\\ ", 
        'EMOT06': '\:\(\(\(', 
        'EMOT07': '\:D', 
        'EMOT08': 'D\:',
        'EMOT09': '\:p', 
        'EMOT10': '\:P',
        'EMOT11': '\:3 ',
        'EMOT12': '\:\\\\', 
        'EMOT13': '\:c',
        'EMOT14': '\;\)',
        'EMOT15': '\;3',
        'EMOT16': '\:oP', 
        'EMOT17': '\:\*',
        'EMOT18': "\:\'\(",
        'EMOT19': '\:\-\)', 
        'EMOT20': '\:\-\(',
        'EMOT21':  '\:o',
        'EMOT22': '\:O',
        'EMOT23': '\:\|', 
        'EMOT24': "\:\'\)", 
        'EMOT25': '\:DDD', 
        'EMOT26': '\:\-D'
          }

    for i in range(len(text)):
        for key in emot:
            text[i] = re.sub(emot[key], ' ' + key + ' ', text[i])

    # get rid of reddit formatting stuff
    text = [re.sub('\&\w\w\;', '', x) for x in text]

    # remove punctuation
    text = [" ".join("".join(["" if ch in string.punctuation else ch for ch in x.lower()]).split()) for x in text]
    
    return text