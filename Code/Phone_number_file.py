import random

# Generating two empty lists for storing phone number
all_phone_number = []
phone_no = ''

# loop for to store 20k phone in the all_phone_number list
for i in range(10):
    # first digit of the number
    no = random.randint(6, 9)
    phone_no.join(str(no))

    # the for loop is used to append the others 9 numbers
    # the others 9 numbers can be in the range of 0 to 9
    for j in range(1, 10):
        no = random.randint(0, 9)
        phone_no.join(str(no))
    # Atlast appending the number into the main file
    all_phone_number.append(phone_no)

print(all_phone_number)
