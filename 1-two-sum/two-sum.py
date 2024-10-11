class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Assumptions:
            - Array will always have two numbers
            - There exists exactly one solution
        Tests:
            nums = [1,1,1,1] target = 2
            output = [0, 1]

            nums = [1, 5, 9, 9] target = 18
            output = [2, 3]

        Approach:
            Brute Force:
                for index_i from 0 to length:
                    for index_j from index_i + 1 to length:
                        add elements at i, j indexes
                        compare with target
                        return if true
                
                time complexity: O(n^2)
                space complexity: O(1)
            Optimal:
                initialize a hashmap
                for i from 0 to length:
                    if value not in hashmap, store hashmap[target - value] i
                    else return i and hashmpa[value]
                
                time complexity: O(n)
                space complexity: O(n)
        '''

        hash_map = {}

        for index, i in enumerate(nums):
            if i not in hash_map:
                hash_map[target - i] = index
            else:
                return [index, hash_map[i]]
        
        return []
        