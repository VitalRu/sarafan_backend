n = int(input())

result: list = []
num = 1
count = 1

while len(result) < n:
    result.extend([num] * count)
    num += 1
    count += 1

    result[:n]

print(' '.join(map(str, result[:n])))
