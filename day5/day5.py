from collections import defaultdict
adj = defaultdict(list)
updates = []
with open("input.txt", 'r') as file:
    build = True
    for line in file:
        if line == '\n':
            build = False
            continue
        
        if build:
            line = line.split('|')
            adj[line[0]].append(line[1].replace('\n', ''))
        else:
            updates.append(line.replace('\n', '').split(','))

#Part 1
def check(up):
    s = set()
    for p in up:
        for pre in adj[p]:
            if pre in s:
                return False
        s.add(p)
    
    return True

#Part 2
def fix(up):
    pass

total, correct = 0, 0
for up in updates:
    if check(up):
        total += int(up[len(up)//2])
    else:
        fix(up)
print(total)
                    