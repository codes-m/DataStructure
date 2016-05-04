arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

max = -100000000
for arr_i in range (1,5) :
    for arr_j in range (1,5) :
        sum = 0
        sum += arr[arr_i][arr_j] 
        sum += arr[arr_i - 1][arr_j ]
        sum += arr[arr_i - 1][arr_j -1]
        sum += arr[arr_i - 1][arr_j + 1]
        sum += arr[arr_i + 1][arr_j ]
        sum += arr[arr_i + 1][arr_j -1]
        sum += arr[arr_i + 1][arr_j +1]
        if(sum > max) :
            max = sum
       
print max
