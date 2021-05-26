# THis Method will provide duplicates we will not be able to eliminate duplicates as the it is auxarray
class auxArray:
    def __init__(self,sum,i,j):
        self.sum = sum
        self.i = i
        self.j = j

def compare(aux1,aux2):
    return aux1.sum -  aux2.sum

def diffrent_index(aux1, aux2):
    if (aux1.i == aux2.i or aux1.i == aux2.j or aux1.j == aux2.i or aux1.j == aux2.j) :
        print('Inside')
        return False
    return True

def solve(arr,n,target):
    size = (n*(n-1))//2

    temp_array = []
    result = set()
    for i in range(n-1):
        for j in range(i+1,n):
            sum = arr[i] + arr[j]
            temp_array.append(auxArray(sum,i,j))

    # print(temp_array)
    temp_array.sort(key=cmp_to_key(compare))
    # for i in temp_array:                  ##Run this loop you will get to know the reason of the duplicates
    #     print(i.sum,i.i,i.j)
    p = 0
    q = size-1

    while(p<q):
        if temp_array[p].sum + temp_array[q].sum == target and diffrent_index(temp_array[p],temp_array[q]):
            result.add((arr[temp_array[p].i],arr[temp_array[p].j],arr[temp_array[q].i],arr[temp_array[q].j]))
            p+=1
            q-=1
        elif temp_array[p].sum + temp_array[q].sum < target:
            p+=1
        else:
            q-=1
    return result