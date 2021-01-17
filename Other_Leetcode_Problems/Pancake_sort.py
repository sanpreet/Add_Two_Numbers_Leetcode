"""
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements 
in the array arr. Write a function pancakeSort(arr) that sorts and 
returns the input array. You are allowed to use only the function flip 
you wrote in the first step in order to make changes in the array.

Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.
"""
import unittest


def max_index_func(arr, k):

	index = 0
	for i in range(k + 1):
		if arr[i] > arr[index]:
			index = i

	return index			


def flip(arr, k):

	pivot = k + 1 // 2
	for i in range(pivot):
		temp = arr[i]
		arr[i] = arr[k - i]
		arr[k - i] = temp


def pancake_sort(arr):

	n = len(arr)

	for i in range(n-1, 0, -1):
		max_index = max_index_func(arr, i)
		flip(arr, max_index)
		flip(arr, i)

	return arr	


class test_cases(unittest.TestCase):

		def cases(self):
			
			desired_output = [1, 2, 3, 4, 5]
			input_arr = [1, 5, 4, 3, 2]
			message ="Case 1"
			self.assertListEqual(desired_output, pancake_sort(input_arr), 
				message)
			
			desired_output = [1, 2]
			input_arr = [1, 2]
			message = "Case 2"
			self.assertListEqual(desired_output, pancake_sort(input_arr), 
				message)	

			desired_output = [1,2,3,4,5,6,7,8,9,10]
			input_arr = [10,9,8,7,6,5,4,3,2,1]
			message = "Case 3: Descending Order"
			self.assertListEqual(desired_output, pancake_sort(input_arr), 
				message)

			desired_output = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,
			7,8,8,8,9,9,9,10,10,10]
			input_arr = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,
			9,8,7,6,5,4,3,2,1]
			message =" Case 4: Repeating digits at different places"
			self.assertListEqual(desired_output, pancake_sort(input_arr), 
				message)

			return "success"


check_case = test_cases()
print(check_case.cases())
