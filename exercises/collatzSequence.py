your_num=int(input("Enter a number:"))
def collatz(number):
    
    if number%2==0:
            print(number//2)
    #elif number%2==1: !!!!!!!!!!!!!!!
            print(3*number+1)
    while number!=1:
        your_num=int(input("Enter a number:"))
        number=your_num


collatz(your_num)


