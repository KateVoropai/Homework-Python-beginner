def fill_cells(N, i, result):
    if N <= 0:
        return []
    if i <= N:
        result.append(i)
        if i == 2 and i != N:
            result.append(-(i-1))
        if 2 < i and i != N:
            result.append(1)
            result.append(-(i-1))
            result.append(-1)
        fill_cells(N, i + 1, result)    
    else:
        fill_cells(N - 2, 1, result)
    return result
    
N = int(input())
i = 1
result = []
print(*fill_cells(N, i, result))