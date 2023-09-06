import math

# functions fibonacci formula: Fn = Fn-1 + Fn-2
def fibonacci(n):
    if n <= 0 :
        return 0
    elif n ==1 :
        return 1
    else:
        return fibonacci(n - 1 ) + fibonacci(n - 2)
    
#input from the user
n = int(input("ENter the value of n: "))
    
#check user input 
if n < 0 :

    print("Please enter a non- negative integer.")
else:
    result = fibonacci(n)
    
#print result 
print(f"The {n}th Fibonacci number is : {result}")

#input from the user=====
print("==Squared calculate==")
print("Please enter a non- negative integer ")
x = int(input("Number X:"))
y = int(input("Number Y:"))
#formula
xyresult = math.pow(x,y)
#print result
print ("The result is : ", xyresult)

#input from the user=====
print("==Greatest common divisor calculate==")
print("Please enter a non-negative integer ")
a = int(input("Number a:"))
b = int(input("Number b:"))
#formula
abresult = math.gcd(a,b)
#print result
print (f"The GCD of {a} and {b} is {abresult}")

#input from the user====
print("==Square root calculate==")
print("Please enter a non-negative integer ")
sr = int(input("Number X:"))
#formula
srresult = math.sqrt(sr)
#print result
print (f"The square root of {sr} is {srresult}")

#average grades 
grades = [3.5,1.75,2,5,3,2,1.5]
#calculate student 
total_students = len(grades)
#calculate total grades
total_grades = sum(grades)
#calculate the average grade
average_grade = total_grades / total_students

#print result
print(f"The average grade of {total_students} students is {average_grade:.2f}")