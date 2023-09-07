## example1:
import random
def decision(number):
    if number==1:
        print("One")
    elif number==2:
        print("Two")
    elif number==5:
        print("Five")
    else:
        print("Not Found!")
ans=random.randint(1,6)
var=decision(ans)
print(var)

## example2

def division(number):
    try:
        return 100//number
    except ZeroDivisionError:
        print("Never divide by Zero!")

variable1=division(19)
variable2=division(0)
print(variable1,variable2)
