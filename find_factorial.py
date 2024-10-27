#to find the factorial of a given number The factorial of n is the product of all positive integers less than or equal to n.



def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        
    

num = int(input("Enter the number"))
print(f"The factorial of number {num} is {factorial(num)}")
        
    