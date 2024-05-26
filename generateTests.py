import random

for i in range(1, 101):
    number = 1000

    file_name = "text" + str(i) + ".txt"
    with open(file_name, 'w') as file:
        file.write(str(number) + "\n")
        for j in range(1, number + 1):
            random_number = random.randint(100, 9999)
            file.write(str(random_number) + "\n")
