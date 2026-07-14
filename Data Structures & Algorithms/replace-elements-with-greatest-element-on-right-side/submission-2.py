class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1

        for i in range(len(arr)- 1, -1, -1):

            new_max = max(max_num, arr[i])
            arr[i] = max_num
            max_num = new_max

        return arr


            # current_max = arr[i]
            # arr[i] = max_num
            # if current_max > max_num:
            #     max_num = current_max