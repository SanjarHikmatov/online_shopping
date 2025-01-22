# # # from django.test import TestCase
# #
# # # Create your tests here.
# #
# #
# #
# # nums = [1,2,2,4,5,5,56,56]
# #
# # asd = []
# # for i in nums:
# #     if i not in asd:
# #         asd.append(i)
# #     if i in asd:
# #         _ = i
# # print(asd)
# def removeDuplicates(nums):
#     # Handle edge case where the list is empty
#     if not nums:
#         return 0
#
#     # Pointer to keep track of where to place the next unique element
#     k = 1
#
#     # Iterate through the array starting from the second element
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:  # If current element is different from the previous one
#             nums[k] = nums[i]  # Place the unique element at the position k
#             k += 1  # Increment the pointer for the next unique element
#
#     # k is the number of unique elements in the array
#     return k
