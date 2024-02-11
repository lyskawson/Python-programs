import re


def strip(text, remove=''):
    
    if remove == '':
        space_regex = re.compile(r'^(\s*)(\S*)(\s)*$')
        mo = space_regex.search(text)
        return mo.group(2)

   
    else:
        removeFront = re.compile(r'^([%s]+)' % remove)
        removeEnd = re.compile(r'([%s]+)$' % remove)
        front = removeFront.search(text)
        end = removeEnd.search(text)
      
        try:
            return text[len(front.group()):len(text) - len(end.group())]
        except AttributeError:
            error_avoid = remove + text + remove
            return strip(error_avoid, remove)


