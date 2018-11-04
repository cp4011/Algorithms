import sys

def rank(list, start, end):
    if start > end:
        return
    base_value = list[start]
    i, j = start, end
    while i < j:
        while i < j and list[j] >= base_value:
            j = j - 1
        while i < j and list[i] <= base_value:
            i = i + 1
        list[i], list[j] = list[j], list[i]
    list[start], list[i] = list[i], list[start]
    rank(list, start, i-1)
    rank(list, i+1, end)

data_file = sys.argv[1]
f = open(data_file, 'r')
list_test = []
for line in f:
    number = float(line.strip('\n'))
    list_test.append(number)

n = 1
k = list_test[0]
rank(list_test, 1, (len(list_test)-1))
for a in list_test[::-1]:
    if n == k:
        print(a, end='')
        break
    else:
        print(a, end=',')
    n = n + 1
