my_file = open("FileOutputDirectory/test_file.txt", "w") # Creates file if file does not exist.
my_file.write("First Line\n")
my_file.write("Second Line\n")
my_file.write("Third Line")

my_file = open("FileOutputDirectory/test_file.txt")         # "r"/read is the default mode
content = my_file.read()
print(content)

my_file.close()



# post_address_file = open("post_address_file", "w")

# post_address_file.write("Marius Conradi Nitschke\n")
# post_address_file.write("Slalomveien 11D\n")
# post_address_file.write("1350 Lommedalen\n")
# post_address_file.write("Norway\n")

# post_address_file.close()
