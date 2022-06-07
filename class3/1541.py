s = input()
a = s.split('-')        # 빼기를 기준으로 나누기
res = []
for ele in a:
    b = ele.split('+')  # 더하기를 기준으로 나누기
    sum_plus = 0
    for i in b:         # 나누어진 수들을 더하기
        sum_plus += int(i)
    res.append(sum_plus)

n = res[0]      # 첫째값에서 빼주어야 하므로

for i in range(1, len(res)):
    n -= res[i]

print(n)