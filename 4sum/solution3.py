#This method is only best for finding the one outcome it can return all the possible outcomes

def diffrent_index(aux1, aux2):
    if (aux1[0] == aux2[0] or aux1[0] == aux2[1] or aux1[1] == aux2[0] or aux1[1] == aux2[1]) :
        # print('Inside')
        return False
    return True

def solve(arr,n,target):
    hash_map ={}
    # arr.sort()
    counter = [0]*n
    for i in range(n-1):
        for j in range(i+1,n):
            temp = arr[i] + arr[j]
            hash_map[temp] = [i,j]

    

    result = []
    
    for i in range(n-1):
        for j in range(i+1,n):
            temp = arr[i]+arr[j]
            if target - temp in hash_map :
                p = hash_map[target-temp]
                if (counter[i]==0 and counter[j]==0 and counter[p[0]]==0 and counter[p[1]]==0 and 
                p[0]!=i and p[1]!=i and p[0]!=j and p[1]!=j ):
                    result.append((arr[i],arr[j],arr[p[0]],arr[p[1]]))
                    counter[i] = counter[j] = counter[p[0]] = counter[p[1]] =1
                    
    return result
                




if __name__ == '__main__':
    arr = [1,0,-1,0,-2,2]
    n = len(arr)
    print(solve(arr,n,0))
    