# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
shoe_list = input()
shoe_list = [int(i) for i in shoe_list.split(' ')]
shoe_counter = Counter(shoe_list)

m = input()
#buy_list = []
total_sale = 0

for k in range(int(m)):
    temp = [int(i) for i in input().split(' ')]
    if shoe_counter.get(temp[0]) and shoe_counter.get(temp[0]) > 0:
        total_sale += temp[1]
        shoe_counter[temp[0]] -= 1
print(total_sale)
