num_numbers = input('Enter a number: ')
num_numbers = int(num_numbers)
num_list = []

for i in range(num_numbers):
    user_input = float(input(f'Enter number {i+1}: '))
    num_list.append(user_input)

print(f'List: {num_list}')