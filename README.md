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
  
Question 2: Check whether permutation palindrome of a string. Code idea goes to [LucidProgramming](https://www.youtube.com/watch?v=dCnxQGMpKz0). There are two concepts to check permutation palindrome of the string and these are as below.  
* Atmost single character can have count of one.  
* Rest all characters have count of two or multiple of two.  

See the below image to understand the concept in detail.    

![palindrome_permutation](https://user-images.githubusercontent.com/3431730/104806661-33119780-57ff-11eb-8a9f-8ab5da8a3a90.jpg)  

### Pancake Problem  

#### Time complexity:    

For function **flip**: Complexity is O(k // 2) which is O(k).  
             **max_index_func**: Complexity is O(n)
             **pancake_sort**: Complexity is O(n)  
             Overall complexity is O(n**2)    

#### Space Complexity
No auxiliary space is used for the program in any of the functions so it is O(1)  

![pancakesort](https://user-images.githubusercontent.com/3431730/104834478-8f3eef00-58c5-11eb-9002-618e4598a108.jpg)
