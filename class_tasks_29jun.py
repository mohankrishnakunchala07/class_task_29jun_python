'1.sum of even numbers (10 to 20)'

Total=0
for i in range(10,21):
    if i%2==0:
        Total=Total+i
print(f"sum of even numbers(10 to 20):",Total)
# output:
# sum of even numbers(10 to 20): 90
'2.sum of odd numbers (10 to 20)'
total_sum=0
for i in range(10,21):
    if i%2==1:
        total_sum=total_sum+i
print(f"sum of odd numbers:{total_sum}")

# output:
# sum of odd numbers:75

'3.Multiplication of even numbers (10 to 20)'

num=int(input("enter number:"))
Total=1
for i in range(10,num+1):
    if i % 2==0:
        Total=Total * i
print(f"Multiplication of even numbers:{Total}")
# output:
# enter number:20
# Multiplication of even numbers:9676800

'4.multiplication of odd numbers (10 to 20)'

num = int(input("enter number: "))
Total=1
for i in range(10,num+1):
    if i % 2==1:
        Total = Total * i
print(f"Multiplication of odd numbers:{Total}")
# output"
# enter number: 20
# Multiplication of odd numbers:692835

'5.Perfect Number'
n=int(input("enter number: "))

Total=0
for i in range(1,n):
    if n%i==0:
        Total=Total+i
if Total==n:
    print("perfect number")
else:
    print("Not a perfect number")
# output:
# enter number: 28
# perfect number