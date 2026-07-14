class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1

        for i in range(len(arr)- 1, -1, -1):
            current_max = arr[i]
            arr[i] = max_num
            if current_max > max_num:
                max_num = current_max

        return arr

