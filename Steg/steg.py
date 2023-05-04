# this program was created by Matthew Mahan for team Pterodactyl 

import copy

def hide_by_bytes(wrapper, payload, offset, interval):

	# make a copy of the wrapper
	modified_wrapper = copy.deepcopy(wrapper)

	# first, find the indexes of bytes which will be replaced in the wrapper 
	replace_indexes = range(offset, (len(payload) * interval) + offset, interval)

	# next is to swap each byte at the above indexes in the wrapper with the sequential bytes of the payload
	# for this, it is more convenient to refer to them by a sequential index
	for i in range(len(replace_indexes)):
		modified_wrapper[replace_indexes[i]] = payload[i]

	return modified_wrapper

def hide_by_bits(wrapper, payload, offset, interval):

	# make a copy of the wrapper
	modified_wrapper = copy.deepcopy(wrapper)

	# first, find the indexes of bytes which will be replaced in the wrapper
	replace_indexes = range(offset, (len(payload) * interval * 8) + offset, interval)

	# separate the payload bytes into bits and put those bits into LSB of bytes for later math
	payload_bytes = bytearray(len(payload * 8)) # this makes a bytearray of all 0x00 for the size of the payload * 8
	for i in range(len(payload)):
		b_str = format(payload[i], '#010b')[2:]

		for j in range(len(b_str)):
			payload_bytes[(i*8)+j] += int(b_str[j])

	# now make the LSB of every relevant byte in the wrapper a 0 followed by
	# using the LSB byte array from the payload, OR it with the selected bytes from the wrapper
	for i in range(len(replace_indexes)):
		modified_wrapper[replace_indexes[i]] = modified_wrapper[replace_indexes[i]] & 0xfe # sets LSB to 0
		modified_wrapper[replace_indexes[i]] = modified_wrapper[replace_indexes[i]] | payload_bytes[i]

	return modified_wrapper

def pdf_test(wrapper_input_filename, payload_input_filename):

	# create/obtain necessary pieces of data 
	sentinel_bytes = bytearray(b'\x00\xff\x00\x00\xff\x00')

	wrapper_file = open(wrapper_input_filename, 'rb') # 'rb' == read as bytes 
	wrapper_data = bytearray(wrapper_file.read())
	wrapper_file.close()

	payload_file = open(payload_input_filename, 'rb') # 'rb' == read as bytes
	payload_data = bytearray(payload_file.read())
	payload_file.close()

	# append sentinel to payload
	payload_data = payload_data + sentinel_bytes

	if DEBUG:
		print(f"Wrapper slice: \n{wrapper_data[1500:1550]}\n")
		# print(f"Payload slice: \n{payload_data[len(payload_data)-100:]}\n")
		# print(f"Sentinel bytes: \n{sentinel_bytes}\n")
		# print(f"Test data bytes: \n{test_data}\n")

	# test hiding by whole bytes
	bytes_modified_wrapper = hide_by_bytes(wrapper_data, payload_data, 100, 8)

	if DEBUG:
		print(f"Wrapper size: {len(wrapper_data)}")
		print(f"Modified size: {len(bytes_modified_wrapper)}")
		print(f"Wrapper slice: \n{wrapper_data[100:160]}\n")
		print(f"Modified slice: \n{bytes_modified_wrapper[100:160]}\n")
		print(f"Modified slice: \n{bytes_modified_wrapper[105:120]}\n")
		print(f"Modified slice: \n{bytes_modified_wrapper[:100]}\n")

	# save the resulting file
	with open('result_bytes.bmp', 'wb') as result_file:
		result_file.write(bytes_modified_wrapper)

	# test hiding by single bits
	bits_modified_wrapper = hide_by_bits(wrapper_data, payload_data, 100, 8)

	if DEBUG:
		print(f"Wrapper size: {len(wrapper_data)}")
		print(f"Modified size: {len(bits_modified_wrapper)}")
		print(f"Wrapper slice: \n{wrapper_data[100:120]}\n")
		print(f"Modified slice: \n{bits_modified_wrapper[100:120]}\n")

	# save the resulting file 
	with open('result_bits.bmp', 'wb') as result_file:
		result_file.write(bits_modified_wrapper)
	

def main():
	pass

if __name__ == "__main__":
	DEBUG = True
	main()
	if DEBUG:
		pdf_test('kinda_big_wrapper.bmp', 'not_tiny_payload.gif')