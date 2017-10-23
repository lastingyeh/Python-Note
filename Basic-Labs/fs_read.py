file = open('my file.txt', 'r')
content = file.readlines()  # read all line into list []

line1 = file.readline()
line2 = file.readline()

print(content)

print(line1)
print(line2)
