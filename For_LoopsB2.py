1.

def Biggie_Size(list):
    for X in range(len(list)):
        if list[X]>0:
           list[X]='big'
    return list
print(Biggie_Size([-1, 3, 5, -5]))


2.
def count_positives(list):
    A = 0
    for val in list:
        if val > 0:
            A += 1
    list[len(list)-1] = A
    return list
print([1,6,-4,-2,-7,-2])
print(count_positives([1,6,-4,-2,-7,-2]))

3.
def sum_total(list):
    sum = 0
    for X in list:
        sum += X
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


4.
def Average(list):
    sum = 0
    for X in list:
        sum += X
    return (sum/len(list))
print(Average([1,2,3,4]))


5.
def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))

6.
def min(list):
    if len(list)<0:
        return False
    minInt = list[0]
    for X in list:
        if X<minInt:
            minInt = X
    return minInt
print(min([37,2,1,-9]))


7.
def Max(list):
    if len(list)<0:
        return False
    MaxInt = list[0]
    for X in list:
        if X>MaxInt:
            MaxInt = X
    return MaxInt
print(Max([37,2,1,-9]))

8.
def Ultimate_Analysis(list):
    dictionary = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximun': list[0], 'length': len(list)}
    for X in list:
        if dictionary['minimum']<X:
            dictionary['minimum'] = X
        if dictionary['maximun']>X:
            dictionary['maximun'] = X
        dictionary['sumTotal']+=X
        dictionary['average']=dictionary['sumTotal']/len(list)
    return dictionary
print(Ultimate_Analysis([37,2,1,-9]))

9.
def Reverse_List(list):
    for X in range(0, (len(list)-1)//2):
        temp = list[X]
        list[X] = list[len(list)-1-X]
        list[len(list)-1-X] = temp
    return list
print(Reverse_List([37,2,1,-9]))