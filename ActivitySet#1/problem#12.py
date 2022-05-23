# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+?@\S+', s)
print(lst)