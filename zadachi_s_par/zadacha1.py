#дан массив целых чисел, для которого нужно узнать,
# какое положительное число является первым отсутствующим
# в ряду натуральных чисел. Предполагается, что массив гарантированно
# удовлетворяет условию единственности такого числа
# (не более одной "дырки" в натуральной части), а также НЕ является отсортированным


print()

l=[3, 2, -2, 4]
z=l[0]
ll=len(l)
for n in range(ll+1):
    if l[n]<0:
        pass
    elif n in l:
        pass
    elif n != 0:
        print(n)
        break

l=list(set(range(1000)) - {4})
z=l[0]
ll=len(l)
for n in range(ll+1):
    if (l[n]<0) & (n in l) & (n != 0):
        print(n)
        break



#def solution1():

#assert solution1([4, 6, 1, 5, 2]) == 3
#assert solution1([3, 2, -2, 4]) == 1
#assert solution1(list(set(range(1000)) - {4})) == 4