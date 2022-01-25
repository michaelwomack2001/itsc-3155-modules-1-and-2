value = []
for i in range(10):
    value.append(int(input('Enter a Number: ')))

counter = [0,0,0,0,0,0,0,0,0,0]
unique = []
is_unique = True

for j in range(10):
    for r in value:
        if value[j] == r:
            counter[j] = counter[j] + 1
    

for c in range(10):
    if(counter[c] == 1):
        unique.append(value[c])

print(unique)