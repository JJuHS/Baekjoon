
from collections import defaultdict

while True:
    try:
        word1 = input()
        word2 = input()
        al1 = defaultdict(int)
        al2 = defaultdict(int)
        for i in word1:
            al1[i] += 1
        for j in word2:
            al2[j] += 1
        ans = ''
        ans_li = []

        for i in al1:
            if i in al2:
                ans_li.append(i)
        ans_li.sort()
        for i in ans_li:
            ans += i * min(al1[i], al2[i])
        print(ans)
    except:
        break