from hashlib import md5
from datetime import datetime
import sys

# This function takes a date string in the format defined in the pdf and converts it to epoch time
def parse_time(time):

	split_time = time.split(' ')
	if (len(split_time) != 6):
		raise RuntimeError("Time format should be 6 integers separated by spaces.")

	# format is YYYY, MM, DD, HH, mm, SS
	dt = datetime(year=int(split_time[0]), month=int(split_time[1]), day=int(split_time[2]), hour=int(split_time[3]), minute=int(split_time[4]), second=int(split_time[5]))
	if DEBUG:
		print(int(dt.timestamp()))

	return int(dt.timestamp())

# function performs the required time math and hashing 
def hash_time(epoch, now):

	elapsed_time = now - epoch

	# calcualte the time to encode
	mod_time = elapsed_time - (elapsed_time % 60)

	return md5(md5(str(mod_time).encode()).hexdigest().encode()).hexdigest()

def parse_code(hash_result):

	# produce the code 
	code = ''
	for char in hash_result:
		while len(code) < 2:
			if char.isalpha():
				code = code + char
			break
	for char in reversed(hash_result):
		while len(code) < 4:
			if char.isdigit():
				code = code + char
			break
	return code

def test(epoch, now, expected_hash, expected_code, test_run=1):

	# find the time of the epoch YYYY MM DD HH mm SS
	epoch_timestamp = parse_time(epoch)
	# find the time of the "current" time 
	current_timestamp = parse_time(now)

	# produce the hash and check
	result = hash_time(epoch_timestamp, current_timestamp)
	
	print(result)
	print(expected_hash)
	# print("Hash as expected?", result == expected_hash)

	# produce the code and check 
	code = parse_code(result)
	print(code)

	return (code == expected_code)

def pdf_examples():

	## TEST 1 
	test_num = 1
	epoch = '1999 12 31 23 59 59'
	current_time = '2013 05 06 07 43 25'
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'ee93'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num))

	## TEST 2 
	test_num = 2
	epoch = '2017 01 01 00 00 00'
	current_time = '2017 03 23 18 02 06'
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'fa51'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num))

	## TEST 3
	test_num = 3
	epoch = '1999 12 31 23 59 59'
	current_time = '2017 04 23 18 02 30'
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'ca45'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num))

	## TEST 4
	test_num = 4
	epoch = '2001 02 03 04 05 06'
	current_time = '2010 06 13 12 55 34'
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'dd15'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num))

	## TEST 5
	test_num = 5
	epoch = '2015 01 01 00 00 00'
	current_time = '2015 05 15 14 00 00'
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'ba26'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num))

# function for handling epoch-related options
def options_epoch(op):

	# D = Default behavior is to read from stdin
	# -E = -E "<YYYY MM DD HH mm SS>" will change behavior to accept epoch from args
	# -7 = -7 will change behavior to use "1970 01 01 00 00 00"

	# get index of this option in the list
	op_index = sys.argv.index(op)

	valid_modes = { '-E': (lambda : parse_time(sys.argv[op_index+1])), \
					'-7': (lambda : 0) }

	return valid_modes[op]()

# discover the options used and set the epoch start accordingly 
def options():

	if DEBUG:
		print(sys.argv)

	epoch = -1
	now = datetime.now().timestamp()
	for op in sys.argv:
		if op in ['-E', '-7']:
			epoch = options_epoch(op)

		# option -c will allow the user to input a string containing the "now" they want to use
		if (op == '-c'):
			op_index = sys.argv.index(op)
			now = parse_time(sys.argv[op_index+1])

	if epoch == -1:
		epoch = parse_time(sys.stdin)

	return (epoch, now)

def main():

	# get the times to use
	epoch, now = options()

	# produce the hash
	result_hash = hash_time(epoch, now)

	# produce the code and print
	code = parse_code(result_hash)
	print(code)

if __name__ == "__main__":
	DEBUG = False
	main()
	# pdf_examples()