grid = []
with open("input.txt", 'r') as file:
    for line in file:
        grid.append(line.replace('\n', ''))

#Part 2
dirs = [(1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, 1), (0, -1)]
s = "XMAS"
def dfs(r, c, i, d):
    if grid[r][c] != s[i]:
        return 0
    if i == len(s)-1:
        return 1
    
    dr, dc = d
    dr += r
    dc += c
    if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
        return dfs(dr, dc, i+1, d)
    return 0

num = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        for dr, dc in dirs:
            num += dfs(i, j, 0, (dr, dc))

print(num)

#Part 2
num = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        acheck = grid[i][j] == 'A'
        ms = [grid[i+1][j+1], grid[i-1][j-1], grid[i+1][j-1], grid[i-1][j+1]]
        mscheck = ms.count('M') == 2 and ms.count('S') == 2
        diag = grid[i+1][j+1] != grid[i-1][j-1]
        if acheck and mscheck and diag:
            num += 1
print(num)