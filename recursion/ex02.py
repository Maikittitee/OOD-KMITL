
def	quick_sort(nums: list) -> list: 
    # base case
    if (len(nums) <= 1):
        return (nums)
    return (quick_sort(list(filter(lambda n: n > nums[0], nums[1:]))) + [nums[0]] + quick_sort(list(filter(lambda n: n <= nums[0], nums[1:]))))
    
        
inp = list(map(int, input("Enter your List : ").split(',')))
print(f"List after Sorted : {quick_sort(inp)}")
 