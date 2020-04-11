def pairs(x, y):
    count = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] ** y[j] > y[j] ** x[i]:
                count += 1

    return count


x = [2, 1, 6]
y = [1, 5]

print(pairs(x, y))
