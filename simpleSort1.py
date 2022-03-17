
def simpleSort1(data):
    for i in range(len(data)):
        j = i
        for k in range(i, len(data)):
            if data[j] > data[k]:
                j = k

        # swap
        tmp = data[i]
        data[i] = data[j]
        data [j] = tmp

    return data


sortedList = simpleSort([1, 4, 2, 7, 9, 3, 1, 13, 6])
print(sortedList)