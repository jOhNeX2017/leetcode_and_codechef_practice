def plusOne(self, arr: List[int]) -> List[int]:
    n = len(arr) -1

    while n >=1:
        if arr[n]<9:
            arr[n]+=1
            break
        else:
            arr[n]=0
        n-=1

    if n==0:
        if arr[0] < 9:
            arr[0]+=1
        else:
            arr.append(0)
            arr[0] = 1

    return arr