obj = [3, 4, 1, 2]

n = len(obj)
for i in range(n-1):
    index = i
    for j in range(i+1,n):
        if obj[i] < obj[j]:
            obj[j], obj[i] = obj[i], obj[j]
