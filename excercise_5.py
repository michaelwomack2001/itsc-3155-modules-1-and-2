num_list1 = []
num_list2 = []
common_list = []

for i in range(5):
    num_list1.append(int(input('Enter a number for the first list: '))) 

for j in range(5):
    num_list2.append(int(input('Enter a number for the second list: '))) 

c = 0
for r in num_list1:
    if r == num_list2[c]:
        common_list.append(num_list2[c])
    c+=1


print(common_list)