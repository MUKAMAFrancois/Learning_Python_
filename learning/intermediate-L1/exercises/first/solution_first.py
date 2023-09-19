"""
6. Write a Python class Inventory with attributes 
like item_id, item_name, stock_count, and price, 
and methods like add_item, update_item, 
and check_item_details.

Use a dictionary to store the item details, 
where the key is the item_id and the value is 
a dictionary containing the item_name, stock_count, 
and price."""

class Inventory:
    def __init__(self):
        self.item={}

    def add_item(self,id,name,stock_count,price):
        self.item[id]={
            'name':name,
            'stock_count':stock_count,
            'price':price
        }

    def show_details(self,id):
        if id in self.item:
            #return f"Product_Name:{self.item[id]['name']},Stock_count:{self.item[id]['stock_count']},Price: {self.item[id]['price']}"
            print(self.item)
        else:
            return "Item Not Found"
        
    def update_item(self,id,name,stock_count,price):
        if id in self.item:
            self.item[id]['name']=name
            self.item[id]['stock_count']=stock_count
            self.item[id]['price']=price

            return self.item
        
Inventory1=Inventory()
Inventory1.add_item('I1',name='Rice',stock_count='Account1',price='$23')
Inventory1.add_item('I2',name='Maize',stock_count='Account2',price='$233')
Inventory1.add_item('I3',name='Sugar',stock_count='Account3',price='$45')
Inventory1.add_item('I4',name='Juice',stock_count='Account4',price='$93')

#update
Inventory1.update_item('I3','SugarCanes','Acc2','$7')
print(Inventory1.show_details('I1'))

"""Q3.

3. Write a Python class Employee with attributes like emp_id, 
emp_name, emp_salary, and emp_department and methods 
like calculate_emp_salary, 
emp_assign_department, and print_employee_details.
"""

class Employee:

    def __init__(self):
        self.employee={}

    def add_employee(self,id,name,
                     hoursWeek,
                     salary,
                     department):
        
        self.employee[id]={
            "name":name,
            "hoursWeek":hoursWeek,
            "salary":salary,
            "department":department
        }

  
    
    def employee_details(self,id):
        if id in self.employee:
            print(self.employee[id])
        else:
            print("No such Employee")
          

    def overtime_amount(self,id,hoursWeek,salary):
        if id in self.employee:
            if hoursWeek>50:
                overtime=hoursWeek-50
                Amount_overtime=(overtime*(salary/50))

                print("Amount Overtime: ",Amount_overtime)
            else:
                print("Your hours less than 50")
        else:
            print("Id not found")
            


"""QN. Write a program to get all possible unique
subsets from a set of distinct integers
"""

class Python_Solution:
    
    def make_subsets(self,current,sets):
        if sets:
            return self.make_subsets(current,sets[1:]) + self.make_subsets(current+[sets[0]],sets[1:])
        return [current]
    def sub_sets(self,sets):
        return self.make_subsets([],sorted(sets))
    

print(Python_Solution().sub_sets([1,2,3]))

"""
1. Write a Python class to find a pair of elements 
(indices of the two numbers) 
from a given array whose sum equals a specific target number.
Note: There will be one solution 
for each input and do not use the same element twice.
Input: numbers= [10,20,10,40,50,60,70], 
target=50
Output: 3, 4
"""
# To do this, Take first number in list and add it to each number in list
# to see if you hit the target. Repeat process for the second number, and so on.

class Target_Addition_List:

    def two_numbers(self,lis):
        target=int(input("Target: "))

        for number in lis:# each number
            # consider each index in list 
            for index in range(len(lis)):

                if number + lis[index] == target:

                    print(f"Indexes: [{lis.index(number)},{index}]")


print(Target_Addition_List().two_numbers([4,6,5,10,-30,40]))


"""
2. Write a Python class to find the three elements 
that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""

class ThreeSum:
    @staticmethod
    def find_three_sum(nums):
        nums.sort()  # Sort the input array in ascending order
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Set two pointers

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Example usage:
if __name__ == "__main__":
    input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
    three_sum = ThreeSum()
    result = three_sum.find_three_sum(input_array)
    print(result)
