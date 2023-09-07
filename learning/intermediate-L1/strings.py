# Lets continue chap 6, MANIPULATING STRINGS

#A. WORKING WITH STRINGS
#1. Escape characters: \n, \",\',\t,\\.
spam="Say Hi! to Bob\'s mother"

#2. Slicing and Indexing
spam[::-1]
spam[5:]

#3. The in operator
"Say" in spam #print: True

#B. STRING METHODS

#1. The upper(), lower(), isupper(),
#  and islower() String Methods

srt='I will love you!'
srt.isupper() # False
srt.upper() # I WILL LOVE YOU!

#2. is...X() methods

srt1='A Thousand Reasons To Learn.'
srt1.istitle() #True
'123'.isdecimal() # True


#isalpha,isspace,isdecimal, isalnum,
# So useful when validating user input

#ex;

while True:
    print('Enter your age:')
    age=input()
    if age.isdecimal():
        break
    print('Please, age must be an integer')



while True:
 print('Select a new password (letters and numbers only):')
 password = input()
 if password.isalnum():
    break
 print('Passwords can only have letters and numbers.')

#3. The startswith() and endswith() String Methods

sp='DRC is country'
sp.startswith('drc') # False

#4. The join() and split() String Methods

print(' '.join(['How', 'are', 'you?']))# How are you?
','.join(['Apple', 'Mango','Juice']) # Apple,Mango,Juice

'The '.join(['Magazine', 'Apart', 'His' ,'Joy']) #MagazineThe ApartThe HisThe Joy


# the split does the opposite

"My name is Simon".split()  #['My', 'name', 'is', 'Simon']

#Sometimes you may want to strip off whitespace characters (space, tab, 
#and newline) from the left side, right side, or both sides of a string. The 
#strip() string method will return a new string without any whitespace
#characters at the beginning or end. The lstrip() and rstrip() methods 
#will remove whitespace characters from the left and right ends, respectively.

spam="        Hello        "
print(spam.rstrip()) # or lstrip() or strip()




### THE RELATED PROJECTS######


