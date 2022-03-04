first=1
second=1
zero=1
x=4000000
sum=0
for n in range(x):
    if zero<x:
        print(zero)
        if zero % 2 == 0:
            sum = sum + zero
        first=second
        second=zero
        zero=first+second

print("Otvet:",sum)

