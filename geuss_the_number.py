# ... This area is to Import Modules.
import myModule as myM
# ... This area is to Define Functions.
random = myM.random

# ... This area is to Code.
myM.start()

print('|==> Geuss The Number <==|')

# range_of_number_A = int(input('Enter your range of A number : '))
# range_of_number_B = int(input('Enter your range of B number : '))

range_of_number_A = int(1)
range_of_number_B = int(10)

print(f'Your range is {range_of_number_A} : {range_of_number_B}.')

random_number = random.randrange(range_of_number_A,range_of_number_B)

# print(f'your random number between ({range_of_number_A}:{range_of_number_B}) is ({random_number})')




myM.exit()