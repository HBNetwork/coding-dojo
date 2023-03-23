'''
DATA: 22/03/2023
FONTE: Leetcode
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [2,11,7,15], target = 9
Output: [0,2]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Participantes:
 - Vitor Pestana
 - Cássio
 - Márcio Contado
 - Fred
 - Everton Matos
 - Greg
 - 

'''

import pytest

def two_sum(array, target):
    
  if len(array) < 2:
      raise ValueError('The length of the "array" must be higher or equals to 2')

  if len(array) > 10**4:
      raise ValueError('The length of the "array" must be lower or equals to 104')
  
  if not -10**9 <= target <= 10**9:
      raise ValueError('Error')

  if min(array) < -10**9:
      raise ValueError('Error')

  if max(array) > 10**9:
      raise ValueError('Error')
      
  # for key, element in enumerate(array):
  #   if array[key] + array[key + 1] == target:
  #       return [key, key + 1]

  resp = []
  for i,x in enumerate(array):      
    for j,y in enumerate(array):
        #print(f'i={i}, x={x}, j={j}, y={y}')
        if not i == j:
            if (x + y) == target and not [j, i] in resp:
                resp.append([i,j])
               

  if len(resp) != 1:
      raise ValueError('Error')
  return resp[0]


def test_two_sum():
  assert(two_sum([2,7,11,15], 9)) == [0, 1]
  assert(two_sum([3,2,4], 6)) == [1, 2]
  assert(two_sum([3,3], 6)) == [0, 1]
  assert(two_sum([3,2,3], 6)) == [0, 2]
  assert(two_sum([2222222,2222222],4444444)) == [0, 1]
  
  with pytest.raises(ValueError):
        two_sum([], 0)
      
  with pytest.raises(ValueError):
        two_sum([1], 0)

  with pytest.raises(ValueError):
        two_sum([1,2], 110)

  with pytest.raises(ValueError):
        two_sum([-110,1], 0)

  with pytest.raises(ValueError):
        two_sum([1,110], 0)

  with pytest.raises(ValueError):
        two_sum([-110,110], 110**10)

  with pytest.raises(ValueError):
        two_sum([3,3,3], 6)

  with pytest.raises(ValueError):
        two_sum([2, 7, 9, 2], 6)
    
if __name__ == "__main__":
    pytest.main(['-svv', __file__])
