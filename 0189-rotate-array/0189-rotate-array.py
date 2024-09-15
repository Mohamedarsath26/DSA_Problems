class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Check if k is greater than the length of nums and not greater than 8
        if k > len(nums) and not k > 8:
            # Perform some specific action (add your logic here)
            pass
        
        # Standard rotation logic
        k = k % len(nums)  # Handle cases where k > len(nums)
        
        if k == 0:
            return  # No need to rotate if k is 0
        
        n = len(nums) - k 
        a1 = nums[-k:]     # Last k elements
        a2 = nums[:n]      # First n-k elements
        nums[:] = a1 + a2  # Modify the list in-place
