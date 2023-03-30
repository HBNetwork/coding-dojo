"""
Find the Index of the First Occurrence in a String #28
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

- Vitor Pestana 
- Cassio augusto
- Greg
- Everton Matos
- Conrado
- João m.    
- Luiz Carlos
- 
"""
import pytest
import random


def fatorial(number):
    result = 1
    for x in range(1, len(number) + 1):
        result *= x
    return result


def permutar(array):
    #"Pn = n!"
    array_final = []

    if len(array) == 1:
        return [array]    
    else:
        total_permutacao = fatorial(array)
        while len(array_final) < total_permutacao:
            random.shuffle(array)
            if array not in array_final:
                array_final.append(array.copy())
        return sorted(array_final)


def test_permutar():
    assert fatorial([1, 2]) == 2
    assert fatorial([1, 2, 3]) == 6
    assert fatorial([1, 2, 3, 4, 5]) == 120
    assert permutar([0]) == [[0]]
    assert permutar([0, 1]) == sorted([[0, 1], [1, 0]])
    assert permutar([2, 1]) == sorted([[2, 1], [1, 2]])
    assert permutar([1, 2, 3]) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1],
                                   [3, 1, 2], [3, 2, 1]])
    assert permutar([1, 2, 3, 4]) == sorted([[1,2,3,4], [1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2], [2,1,3,4], [2,1,4,3], [2,3,1,4], [2,3,4,1], [2,4,1,3], [2,4,3,1], [3,1,2,4], [3,1,4,2], [3,2,1,4], [3,2,4,1], [3,4,1,2], [3,4,2,1], [4,1,2,3], [4,1,3,2], [4,2,1,3], [4,2,3,1], [4,3,1,2], [4,3,2,1]])


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
