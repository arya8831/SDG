from itertools import permutations
from faker import Faker
import csv
import time

# Name of the fields
fields = ['Name', 'Date of Birth', 'Address', 'Email', 'Phone Number']

# Name of the file
file = "Outputs/Data12.csv"

# Generating dictionary
fake = Faker()
phone_number = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10))
# results = []
# for c in (product([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], repeat=6)):
#     results.append(c)
dummy_data = []
# Data rows of the csv file
with open(file, 'w+') as f:
    write = csv.writer(f)
    write.writerow(fields)

    # Inserting data in the csv file
    start_time = time.time()
    c = 1
    for i in range(0, 3628001):
        data = fake_data = []

        # Name
        name = fake.name()

        # Address
        address = fake.address()

        # E-mail id
        email = fake.email()

        # Date of Birth
        dob = str(fake.date_of_birth())

        # Phone Number
        phone_no = phone_number[i]
        s = [str(integer) for integer in phone_no]
        a_string = "".join(s)
        phone_no = a_string

        # # Id Number
        # id_no = results[i]
        # s = [str(integer) for integer in id_no]
        # a_string = "".join(s)
        # id_no = int(a_string)

        data = [name, dob, address, email, phone_no]
        # fake_data.append(data)
        print(c, 'data sent')
        write.writerow(data)
        c += 1
f.close()
print("Total Time taken", time.time() - start_time)
