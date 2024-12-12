#Part 2 lets one level be removed
# def problem_dampner(i, levels, asc):
#     if i == 0 or i == len(levels)-2 or 1 <= abs(levels[i-1]-levels[i+1]) <= 3 and ((asc and levels[i-1] < levels[i+1]) or (not asc and levels[i-1] > levels[i+1])):
#         return True
    
#     return False
    
def is_safe(levels, asc, prob_damp=False):
    for i in range(len(levels)-1):
        if abs(levels[i]-levels[i+1]) < 1 or abs(levels[i]-levels[i+1]) > 3 or (asc and levels[i] > levels[i+1]) or (not asc and levels[i] < levels[i+1]):
            # if prob_damp or not problem_dampner(i, levels, asc):
            #     return False
            # else:
            #     prob_damp = True
            return False
        
    return True

def is_asc(levels):
    asc, desc = 0, 0
    for i in range(len(levels)-1):
        if levels[i] < levels[i+1]:
            asc += 1
        else:
            desc += 1
    
    return asc > desc

safe = 0
with open('input.txt', 'r') as file:
    for line in file:
        levels = [int(n) for n in line.split()]
        if len(levels) <= 3:
            safe += 1
            continue
        
        asc = is_asc(levels)
        
        if is_safe(levels, asc):
            safe += 1
        else:
            for i in range(len(levels)):
                n = levels.pop(i)
                if is_safe(levels, asc):
                    safe += 1
                    break
                levels.insert(i, n)
print(safe)