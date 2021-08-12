# Given an array of items, an i-th index element denotes the item id’s, and given a number m, the task is to remove m elements such that there should be minimum distinct id’s left. Print the number of distinct id’s.
# Input : arr[] = { 2, 2, 1, 3, 3, 3}
#             m = 3
# Output : 1
# Remove 1 and both 2's.So, only 3 will be
# left that's why distinct id is 1.
#
# Input : arr[] = { 2, 4, 1, 5, 3, 5, 1, 3}
#             m = 2
# Output : 3
# Remove 2 and 4 completely. So, remaining ids
# are 1, 3 and 5 i.e. 3
import collections
from typing import List


class Solutin_R1:
        def DistinctCountAfterRemoval(self,nums: List[int] ,removalCount: int) -> int:
            counter = collections.Counter(nums)
            freqs = sorted(counter.values())
            result = len(freqs)
            for freq in freqs:
                if removalCount >= freq:
                    result -= 1
                    removalCount -= freq
                else:
                    break
            return result



def main():
    testObject = Solutin_R1()
    print(testObject.DistinctCountAfterRemoval([1,1, 2,2, 4, 4], 1))

if __name__=="__main__":
    main()