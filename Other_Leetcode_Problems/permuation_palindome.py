import unittest

	
def permutation_palindrome(string_input):
	"""
	Step 1: Preprocessing
	Removing spaces and converting to lower case 
	"""
	string_input = string_input.replace(" ","")
	string_input = string_input.lower()

	hash_table = dict()

	for char in string_input:
		if char in hash_table:
			hash_table[char] += 1
		else:
			hash_table[char] = 1

	count_odd = 0		
	for key, value in hash_table.items():
		if value % 2 != 0 and count_odd == 0:
			count_odd += 1
		elif value % 2 != 0 and count_odd != 0:
			return False
	return True			  		


class test_cases(unittest.TestCase):

	def cases(self):
		desired_output = False
		actual_input = "a bbc"
		self.assertEqual(desired_output, permutation_palindrome(actual_input))
		return "Success..."


check_case = test_cases()
print(check_case.cases())

