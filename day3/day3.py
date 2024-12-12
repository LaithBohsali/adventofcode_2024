buf = ""
with open("input.txt", 'r') as file:
    buf = file.read()

global do
do = True
def check(i):
    global do

    if buf[i:i+4] == "do()":
        do = True
        return False, -1, 0
    
    if buf[i:i+7] == "don't()":
        do = False
        return False, -1, 0
    
    if not do:
        return False, -1, 0


    if buf[i:i+4] != "mul(":
        return False, -1, -1
    j = i+4
    while j < len(buf) and buf[j].isdigit():
        j += 1
    
    if j >= len(buf) or j == i+4 or j-(i+4) > 3:
        return False, -1, -2
    
    n1 = int(buf[i+4:j])
    k = j
    if buf[k] != ',':
        return False, -1, -3
    
    k += 1
    while k < len(buf) and buf[k].isdigit():
        k += 1
    
    if k >= len(buf) or k == j+1 or k-(j+1) > 3:
        return False, -1, -4

    n2 = int(buf[(j+1):k])

    if k < len(buf) and buf[k] == ')':
        return True, n1*n2, k+1
    
    return False, -1, -5

total = 0
i = 0
while i < len(buf):
    res, val, j = check(i)
    if res:
        total += val
        i = j
    else:
        i += 1
print(total)