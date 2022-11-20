'''
Any digit number enetered by user
1. Write a program to reverse that number.
2. Find the sum of digit.

e.g.
n=6778

1st Iteration           2nd iteration         3rd iteration         4th iteration 
n=6778                  n=677                 n=67                  n=6
r=n%10 = 6778%10=8      r=n%10 = 677%10=7     r=n%10 = 6778%10=7    r=n%10 = 6778%10=7
print(8)                print(7)              print(7)              print(6)
n=n//10=6778//10=677    n=n//10=677//10=67  n=n//10=67//10=6     n=n//10=6//10=0

'''


n=int(input("Enter a number "))
while(n!=0) :
    r=n%10
    print(r)
    n=n//10
