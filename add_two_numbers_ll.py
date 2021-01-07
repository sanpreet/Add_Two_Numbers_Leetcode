import unittest
"""
You are given two non-empty linked lists representing two non-negative 
integers The digits are stored in reverse order, and each of their nodes 
contains a single digit. Add the two numbers and return the sum 
as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

"""
Step 1: Create stack for each of the linkedlist. Stack will put the LSB at 
top and MSB at the bottom
"""


class Node:

    def __init__(self, data, next_add):
        self.data = data
        self.next = next_add


class stack_linked_list:

    def __init__(self):

        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def create_stack(self, value):

        node_create = Node(value, None)

        if self.is_empty():
            self.head = node_create
        else:
            node_create.next = self.head
            self.head = node_create

        self.size += 1

    def pop_top_element(self):

        if self.is_empty():
            return
        else:
            e = self.head.data
            self.head = self.head.next

        self.size -= 1

        return e

    def display_ll(self):

        reference = self.head
        while reference:
            print(reference.data, end='-->')
            reference = reference.next
        print()


s1 = stack_linked_list()
s1.create_stack(9)
s1.create_stack(9)
s1.create_stack(9)
s1.create_stack(9)
s1.create_stack(9)
s1.create_stack(9)
s1.create_stack(9)
s1.display_ll()

s2 = stack_linked_list()
s2.create_stack(9)
s2.create_stack(9)
s2.create_stack(9)
s2.create_stack(9)
s2.display_ll()

"""
Step 2: Aim is to get the result in the reverse order that is 
LSB at first position in the list and MSB at the last position in the list.
Concept of modulus and division operator is used to carry out addition
Result is stored in the list as desired.
"""
carry = 0
output = list()
while not s1.is_empty() or not s2.is_empty() or carry != 0:
    sum_var = carry

    if not s1.is_empty():
        sum_var += s1.pop_top_element()
    if not s2.is_empty():
        sum_var += s2.pop_top_element()

    output.append(sum_var % 10)
    carry = sum_var // 10
"""
Step 3: Test Cases are implemented.
"""


class test_cases(unittest.TestCase):

    def cases_implement(self):
        desired_output = [8, 9, 9, 9, 0, 0, 0, 0]
        actual_output = output
        message = "Desired and actual values are not equal"
        self.assertListEqual(desired_output, actual_output, message)
        return "Success..."


check_case = test_cases()
print(check_case.cases_implement())
