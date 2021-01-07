# Add_Two_Numbers_Leetcode
Adding two numbers LinkedList Medium Level Problem  

## Problem Statement     
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.   

You may assume the two numbers do not contain any leading zero, except the number 0 itself.  

Input: l1 = [2,4,3], l2 = [5,6,4]  
Output: [7,0,8]  
Explanation: 342 + 465 = 807.      

Link for the problem:  https://leetcode.com/problems/add-two-numbers/ 

## Intuition for  algorithm  
Since addition of two numbers is required. Some ideas that I thought to implement the solution are as below  

1.) Two numbers to be added can be of same length or different length.  
2.) Addition always takes place from LSB to MSB  
3.) Two Stacks can be used and pop is done from both the stacks. Results is added and if there is carry it is transfered else not.    
4.) When no further carry is transfered or stacks become empty stop the loop.  
5.) List is output which contains LSB first and MSB at the end as this is the requirement of the task.   

## Why LSB first and MSB end in LinkedList  

Since addition of two numbers always take place from LSB and for the linkedlist LSB is the tail, hence for travelling to tail from the head the time
complexity of **O(n)** is needed which is expensive and hence with the help of stacks linkedlist is reversed so that LSB comes at the first position and MSB at the end for the addition to take place. 

## Time and Space Complexity  

Time Complexity

In the code pop is used which takes place in the unit time and then result is appended to the list which takes in O(n) time.  

Total Time: O(1) + O(n) =  O(n) : Droping the constant according to Big O notation rule.  

Space Complexity  

Since the list is used in the code to save the result which will cover extra auxiliary space and hence space complexity of O(n) is taken by the code.
  

