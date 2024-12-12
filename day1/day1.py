import bisect

l1, l2 = [], []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        bisect.insort(l1, int(line[0]))
        bisect.insort(l2, int(line[1]))

#Part 1
# dist = 0   
# for n1, n2 in zip(l1, l2):
#     dist += abs(n1-n2)
#
# print(dist)

#Part 2
sim = 0
dic = {}
j = 0
for i in range(len(l1)):
    if l1[i] in dic:
        sim += dic[l1[i]]*l1[i]
    else:
        while j < len(l2) and l2[j] < l1[i]:
            j += 1
        if j >= len(l2): break

        cnt = 0
        while j < len(l2) and l1[i] == l2[j]:
            j += 1
            cnt += 1
        sim += cnt*l1[i]
        dic[l1[i]] = cnt
print(sim)