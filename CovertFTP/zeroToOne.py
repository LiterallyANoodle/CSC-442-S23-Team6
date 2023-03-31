from sys import *

def convert(contents):

	nums = []
	while contents != '':
		if contents[0] == 'z':
			nums.append('0')
			contents = contents[4:]
		else:
			nums.append('1')
			contents = contents[3:]

		# print(contents)

	return nums

if __name__ == "__main__":

	if len(argv) < 2:
		print("Needs argument of file to read")
		exit()

	filepath = argv[1]

	file = open(filepath)
	contents = file.read()
	file.close()

	# print(contents)

	binaries = convert(contents)
	print(''.join(binaries))
