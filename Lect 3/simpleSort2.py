def simpleSort2(data):
    for i in range(len(data)):
        # 1. find smallest element
        j = findSmallestAfterI(data, i)

        # 2. swap
        data = swap(data, i, j)
    return data


def findSmallestAfterI(data, i):
    j = i
    for k in range(i, len(data)):
        if data[j] > data[k]:
            j = k
    return j


def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp
    return data


sortedList = simpleSort2([1, 4, 2, 7, 9, 3, 1, 13, 6])

print(sortedList)