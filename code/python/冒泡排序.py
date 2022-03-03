obj = [3, 4, 1, 2]


for i in range(len(obj)):
    for j in range(i):
        if obj[j] < obj[j + 1]:
            obj[j], obj[j + 1] = obj[j + 1], obj[j]
