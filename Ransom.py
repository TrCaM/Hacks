from collections import Counter
def ransom_note(magazine, ransom):
    # if len(ransom) > len(magazine):
    #     return False
    # Map = {}
    # for word in magazine:
    #     if word not in Map:
    #         Map[word] = 1
    #     else:
    #         Map[word] += 1
    # for word in ransom:
    #     if word not in Map or Map[word] == 0:
    #         return False
    #     else:
    #         Map[word] -= 1
    # return True

    # Try this collection thing
    return (Counter(ransom) - Counter(magazine)) == {} 
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
