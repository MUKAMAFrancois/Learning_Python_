# 1. Basics
myCat = {'size': 'fat',
          'color': 'gray', 
          'disposition': 'loud'}
# we access dict via keys
#print(f"My Cat is too {myCat['size']} and has color of {myCat['color']}")

#Example 1: 

birthdays={'John':'Apr 1','Mukama':'Aug 1','Kelas':'Dec 12','David':'May 23'}

def listing_bd(dc):
    for name in dc.keys():
        print(f"{name} has birthday of {dc[name]}")

#listing_bd(birthdays)

#Example 2:

while True:
    person=input("Enter a name, (blank to quite):")
    if person =='':
        print('Exited')
        break
    elif person in birthdays.keys():
        print(f"{person} has birthday at {birthdays[person]}")
    else:
        bd=input("I don't have his birthday, enter his bd:")
        birthdays[person]=bd

# Methods for Dictionaries: .items(), .keys(), .get(),...

keys=['ML engineer','Data Analyst','Statician']
values=['$220K','$125K','$20K']
res=dict(zip(keys,values))

for key,value in res.items():
    print(f"{key} ==> has salary of {value}")

#ML engineer ==> has salary of $220K
#Data Analyst ==> has salary of $125K
#Statician ==> has salary of $20K

# You can use get() method to know wether an Item exists in a dictionary!,
#  or pass a zero to be returned if not exist..

print(f" I am getting a salary of {res.get('ML engineer', 0)}")
print(f" I am getting a salary of {res.get('Django developer',0)}")


### The setdefault() method
# It is the nice way to show that a key exists 

#EX: charactercount.py

message='We went to waterfalls in such winters.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]+=1

for k,v in count.items():
    print(f"{k}:{v}")

    


##**Using Data Structures to Model Real-World Things


### Nested dictinonaries,
#Dictionaries can contain other data types like lists or other dicts

# EX3.

shoppings={'John':{'watches':5, 'cars':2, 'Pc':4},
           'Alice':{'watches':8,'cars':3,'Pc':5},
           'Didieu':{'cars':1,'watches':1,'Pc':1}
           }
# suppose we want to know how much items to shop
# you can make a simple function


def all_to_shop(shoppify):
    total_watches=cars=computers=0
    for key, value in shoppify.items():
        total_watches+=shoppify[key]['watches']
        cars+=shoppify[key]['cars']
        computers+=shoppify[key]['Pc']
    
    print('All Items to shop:\n')
    print(f'Wathes:{total_watches}')
    print(f'Cars:{cars}')
    print(f'Computers:{computers}')
    

all_to_shop(shoppings)

                    #All Items to shop:

                        #Wathes:14
                            #Cars:6
                        #Computers:10



