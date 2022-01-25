row = input('Enter a row num from 1 to 5: ')
col = input('Enter a col num from 1 to 5: ')

row = int(row)
col = int(col)

grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
grid[row-1][col-1] = 1

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])
print(grid[4])
