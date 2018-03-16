# --*-- coding: utf-8 --*--

from io import open
import re


prefix = ['คุณ', 'นาย', 'นาง', 'นางสาว']
prefix_regex = ['^' + item.decode('utf8') for item in prefix]

original_content = []
with open('data.csv', 'r', encoding='utf8') as data:
    original_content = data.readlines()

new_content = []
for content in original_content:
    replaced = re.sub('|'.join(prefix_regex), '', content)
    new_content.append(replaced)

with open('new_data.csv', 'w') as writer:
    for content in new_content:
        writer.write(unicode(content))
