import re

pattern = r'\d+'
text = "there are 123 apples with me "
match = re.search(pattern,text)
print(match.group())