def number_needed(a, b):
    count =0
    x = [0]*26
    k= 0;
    for i in list(a):
        x[ord(i) - ord('a')] +=1
    for i in list(b):
        x[ord(i) - ord('a')] -=1
    for j in x:
        count += abs(j)
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))

# Improve into log(a+b) by using a backing array to count the occurences
