# This program was created by Matthew Mahan of team Pterodactyl. 

from hashlib import md5
from datetime import datetime, timezone
import time as t
import pytz
import sys

# This function takes a date string in the format defined in the pdf and converts it to epoch time
def parse_time(time):

	print(f"Input time is {time}")

	split_time = time.split(' ')
	if (len(split_time) != 6):
		raise RuntimeError("Time format should be 6 integers separated by spaces.")


	# format is YYYY, MM, DD, HH, mm, SS
	tz = timezone.utc
	dt = datetime(year=int(split_time[0]), month=int(split_time[1]), day=int(split_time[2]), hour=int(split_time[3]), minute=int(split_time[4]), second=int(split_time[5]))
	print(dt.tzname())
	print(f"Parsed time is {dt.isoformat()}")
	if DEBUG:
		print(f"Time stamp was: {int(dt.timestamp())}")


	# Timo's recommendation: 
	ti = pytz.timezone("America/Chicago").localize(dt)
	print(f"----------> {ti}")
	ti = ti.astimezone(pytz.UTC)
	print(f"----------> {ti}")

	return int(ti.timestamp())

# function performs the required time math and hashing 
def hash_time(epoch, now, expected_elapsed=0):

	elapsed_time = now - epoch

	if DEBUG:
		print(f"Elapsed calc is {elapsed_time}")
		print(f"Expected calc is {expected_elapsed}")
		print(f"Epoch ts is {epoch}")
		print(f"Now ts is {now}")
		# print(f"Diff is {expected_elapsed - elapsed_time}")

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

def test(epoch, now, expected_hash, expected_code, test_run=1, expected_elapsed=0):

	# find the time of the epoch YYYY MM DD HH mm SS
	epoch_timestamp = parse_time(epoch)
	# find the time of the "current" time 
	current_timestamp = parse_time(now)

	# produce the hash and check
	result = hash_time(epoch_timestamp, current_timestamp, expected_elapsed)
	
	print(result)
	print(expected_hash)
	# print("Hash as expected?", result == expected_hash)

	# produce the code and check 
	code = parse_code(result)
	print(code)

	return (code == expected_code)

def pdf_examples():

	print(datetime.utcnow())
	print(datetime.now())

	## TEST 1 
	test_num = 1
	epoch = '1999 12 31 23 59 59'
	current_time = '2013 05 06 07 43 25'
	expected_elapsed = 421_137_806
	expected_hash = '3ee1df13bc19a968b89629c749fee39d'
	expected_code = 'ee93'
	print(f"TEST {test_num} ---------------------------------------------")
	print("Code as expected?", test(epoch, current_time, expected_hash, expected_code, test_num, expected_elapsed))

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
	now = datetime.utcnow().timestamp()
	for op in sys.argv:
		if op in ['-E', '-7']:
			epoch = options_epoch(op)

		# option -c will allow the user to input a string containing the "now" they want to use
		if (op == '-c'):
			op_index = sys.argv.index(op)
			now = parse_time(sys.argv[op_index+1])

	if epoch == -1:
		if DEBUG:
			print(sys.stdin.readlines()[0])
		epoch = parse_time(sys.stdin.readlines()[0])

	return (epoch, now)

def main():

	# get the times to use
	epoch, now = options()

	# produce the hash
	result_hash = hash_time(epoch, now)
	print(result_hash[:len(result_hash)//2])
	print(result_hash[len(result_hash)//2:])
	print(result_hash[len(result_hash)//2])

	# produce the code and print
	code = parse_code(result_hash)
	print(code)

if __name__ == "__main__":
	DEBUG = True
	main()
	# pdf_examples()