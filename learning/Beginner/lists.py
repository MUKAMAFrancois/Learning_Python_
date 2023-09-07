# example1[Mine]
i=0
a=[]
inp=input("Enter sth not empty:")
while inp !='':
    inp=input(f"Enter {i}th or nothing to stop:")
    a.append(inp)
    i+=1

print(a[:-1]) # we removed the last item as it is ''
for j in range(len(a)-1):
    print(f'Index {j} corresponds to:', a[j])

#Example 2: Methods

alist=['Olok',12,45,'Love']
print(alist.index('Love')) #3
alist.insert(0,"first") #['first', 'Olok', 12, 45, 'Love']
print(alist)
alist.remove(12)
spam = [2, 5, 3.14, 1, -7]
list1=['ants', 'cats', 'dogs', 'badgers', 'elephants']
#The sort method works for list of same data type
spam.sort()
print(spam) # [-7, 1, 2, 3.14, 5]


list1.sort()
print(list1) #['ants', 'badgers', 'cats', 'dogs', 'elephants']


spam.sort(reverse=True)
print(spam) #[5, 3.14, 2, 1, -7]

list2=['a', 'z', 'A', 'Z']
list2.sort(key=str.lower)
print(list2) #['a', 'A', 'z', 'Z']



#Example3: References

spam=[1,2,3,4,5]
cheese=spam
cheese[0]='DataScince'
print(spam) #['DataScince', 2, 3, 4, 5]
print(cheese)  #['DataScince', 2, 3, 4, 5]

# all are the same, they don't work as variables.
# thus they point to a reference instead of values.

def fun(someparameter):
    someparameter.append("Hello")

list3=[0,9,8,7]
fun(list3)
print(list3)  #[0, 9, 8, 7, 'Hello']

# To avoid a copy of references between lists and dictionaries, 
#Python provides modules: Copy and deepcopy to copy list values.
 # thus our first example can be written as:


import copy
spam=[1,2,3,4,5]
cheese=copy.copy(spam)
cheese[0]='datascience'

print(cheese) #['datascience', 2, 3, 4, 5]
print(spam) #[1,2, 3, 4, 5]
#cheese = copy.copy(spam) creates a second list that can be modified 
#independently of the first.

#If the list you need to copy contains lists, then use the copy.deepcopy()
#function instead of copy.copy(). The deepcopy() function will copy these 
#inner lists as well.

#LIST COMPREHENSION

numbers=[23,10,90]
cubed=[j**3 for j in numbers] #[12167, 1000, 729000]
print(cubed)



list = [i for i in range(11) if i % 2 == 0]
print(list)



#Nested List comprehension
matrix=[[j for j in range(5)] for i in range(4)]
print(matrix) 
#[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]




# using lambda to print table of 10
numbers = []

for i in range(1, 6):
	numbers.append(i*10)

print(numbers) #[10, 20, 30, 40, 50]

#same as 
numbers = [i*10 for i in range(1, 6)]
print(numbers)
