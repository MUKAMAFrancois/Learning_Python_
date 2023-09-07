from random import randint
computer_guess=randint(1, 10)
print("Guess my number betwen 1 and 10:")
print("You have 4 times to try")
your_guess=int(input("Take a guess:"))

count=0
for j in range(4):
    if your_guess==computer_guess:
        print(f"Congrats, you passed at{count}")

        break
    elif your_guess<computer_guess:
        print("Your guess is too low")
        your_guess=int(input("Take a guess:"))
    else:
        print("Your guess is too high")
        your_guess=int(input("Take a guess:"))
        
    count+=1
 
  
        


   
    

