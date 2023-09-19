
"""
2. Write a Python class to find the three elements 
that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""



def make_subsets_oftwo(lis):
   # target=int(input("Traget: "))
    
    empty2=[]
    for index in range(len(lis)):
        for j in range(len(lis)):
            if lis[j] == lis[index]:
                continue

            empty2.append([lis[j],lis[index]])
            

    print(sorted(empty2))
    

print(make_subsets_oftwo([1,9,5]))


