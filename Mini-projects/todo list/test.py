file = open("tasks.txt", "w")

file.write("Learn Python\n")
file.write("Go Gym\n")
file.write("Buy Milk\n")

file.close()

file = open("tasks.txt", "r")

print(file.read())

file.close

#test file to test the working of file handling fucntions, read and write

#added newly created test file in .gitignore