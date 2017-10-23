text = 'This my file. \nThis is next line.'
append_text = '\nThis is appended file.'

# my_file = open('my file.txt', 'w')
my_file = open('my file.txt', 'a')

my_file.write(append_text)

my_file.close()
