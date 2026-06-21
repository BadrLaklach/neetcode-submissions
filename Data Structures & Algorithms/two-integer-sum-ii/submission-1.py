class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array = []
        l,r = 0,len(numbers)-1

        while len(array) != 2 :

            if numbers[l]+numbers[r] < target :
                l = l + 1
            
            if numbers[l]+numbers[r] > target :
                r = r - 1

            if numbers[l]+numbers[r] == target:
                array.append(l+1)
                array.append(r+1)
                return array             
