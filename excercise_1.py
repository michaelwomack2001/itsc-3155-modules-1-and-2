grade = input('Enter a grade from 0 to 100:')
print(f'You grade is {grade}')

grade = int(grade)

if grade >= 90:
    print('You got an A')
elif grade >= 80:
    print('You got an B')
elif grade >= 70:
    print('You got an C')
elif grade >= 60:
    print('You got an D')
else:
    print('You got a F')