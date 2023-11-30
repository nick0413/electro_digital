def print_all_lines_in_file(file_name):
	
	with open(file_name,"r") as file:
		lines=file.readlines()
		for line in file:
			print(line)

		# length=len()
		print(len(lines))


print_all_lines_in_file("passwords.txt")