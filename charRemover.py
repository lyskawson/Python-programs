#! /usr/bin/env python3

import pyperclip


text = pyperclip.paste()

lines = text.split('\n')
newLines = []

for line in lines:
    index = 0
    for char in line:
        if not char.isdigit() and char != ' ':
            break
        index += 1
    newLines.append(line[index+1:])

text = '\n'.join(newLines)
pyperclip.copy(text)




