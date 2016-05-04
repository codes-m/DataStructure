a = input()
a = int(a)

list_of_all=[]
list_of_query=[]

for i in range (0,a):
    list_of_all.append(raw_input())
for i in range (0,a):
    print list_of_all[i]

b = int(input())

for i in range (0,b) :
    list_of_query.append(raw_input())
for i in range (0,b):
    print list_of_query[i]

for i in range (0,b):
    counter = 0
    for j in range (0,a) :
        if(list_of_query[i] == list_of_all[j] ) :
            counter += 1
    print counter
