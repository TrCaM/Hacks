def array_left_rotation(a, n, k):
    step = k % n
    answer = []
    for i in range(0, n):
        answer.append(a[(i+step)% len(a)])
    return answer

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
