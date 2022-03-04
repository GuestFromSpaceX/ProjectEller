#Простые делители числа 13195 - это 5, 7, 13 и 29.

#Каков самый большой делитель числа 600851475143, являющийся простым числом?

number=600851475143
counter=0
array=[]
for n in range(2,number):
    if number % n == 0:
        for m in range(2,n):
            if (n % m == 0):
                counter=+1
        if counter==0:
            print(n)