a = map(int , raw_input().split(' '))

list_of_sequence = []
for i in range (0,a[0]) :
    temp = []
    list_of_sequence.append(temp)
lastans = 0



for i in range (0,a[1]) :
    query = map(int , raw_input().split(' '))
    if (query[0] == 1 ) :
        index_seq = ( (query[1] ^ lastans ) %  a[0] )
        list_of_sequence[index_seq].append(query[2])
    else :
        index_seq = ( (query[1] ^ lastans ) %  a[0] )
        index_element = (query[2] % len(list_of_sequence[index_seq]))
        lastans = list_of_sequence[index_seq][index_element]
        print lastans

for i in range (0,a[0]) :
    for j in range (0,len(list_of_sequence[i])):
        print list_of_sequence[i][j],
    print
