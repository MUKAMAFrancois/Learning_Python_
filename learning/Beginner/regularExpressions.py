# re module is for regular expression

# 1. INTRODUCTION ****************************
# [1]
import re

s="Data Scientist : Where my future job relies"

searched=re.search(r'future',s) #Note: Here r character (r’portal’) stands for raw, not regex
print(f"Start at index:{searched.start()}")
print(f"It ends at index of: {searched.end()}")

"""  
OUT:
Start at index:26
It ends at index of: 32
"""
#[2]

import re

string = "Django development is good."
pattern="[a-g]" # [a-c] is same as [abc]
result=re.findall(pattern,string)
print(result) #['a', 'g', 'd', 'e', 'e', 'e', 'g', 'd']

#3
#Caret (^) symbol matches the beginning of the string 
# i.e. checks whether the string starts with the given character(s) or not

sentence=["Always be good to anyone","Yeah","Always,i will try"]
regex=r"^Always"
for found in sentence:
    if re.match(regex,found):
        print(f"Yes, Already found:{found}")
    else:
        print("Not found! 404")

"""
OUT:
Yes, Already found:Always be good to anyone
Not found! 404
Yes, Already found:Always,i will try
"""

#4

#Dollar($) symbol matches the end of the string 
# i.e checks whether the string ends with the given character(s) or not.

string = "Hello World!"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
	print("Match found!") # Match found
else:
	print("Match not found.")

# 2. FUNCTIONS******************************
# we are going to see: search, finditer,match, fullmatch,findall,split

# we are comming soon......

