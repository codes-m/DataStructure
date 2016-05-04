n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for i in range (0,len(arr)) :
    print arr[len(arr)-i-1],
