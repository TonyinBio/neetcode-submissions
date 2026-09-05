class Solution:
    def trap(self, height: List[int]) -> int:
        # notice levels increase (not strictly) from outside to inside
        l_ptr = 0
        r_ptr = len(height) - 1

        r_val = height[r_ptr]
        while r_val == 0 and r_ptr > 0:
            r_ptr -= 1
            r_val = height[r_ptr]

        l_val = height[l_ptr]
        while l_val == 0 and l_ptr < len(height) - 1:
            l_ptr += 1
            l_val = height[l_ptr]
        
        width = r_ptr - l_ptr - 1
        if width <= 0: return 0

        water_level = min(l_val, r_val)
        total_water = water_level * width
        best_r_val = r_val
        best_l_val = l_val
        while r_ptr > l_ptr + 1:
            # print(l_ptr, r_ptr, total_water)
            if r_val <= l_val:
                r_ptr -= 1
                r_val = height[r_ptr]
                if r_val > best_r_val:  # can we pour more water?
                    width = r_ptr - l_ptr - 1
                    amt_water_logged = min(l_val, r_val)
                    water_level = amt_water_logged - best_r_val
                    # print(water_level, width)
                    total_water += water_level * width
                    
                    total_water -= best_r_val
                    best_r_val = r_val
                else:
                    total_water -= r_val
                    
            else:
                l_ptr += 1
                l_val = height[l_ptr]

                if l_val > best_l_val:
                    width = r_ptr - l_ptr - 1
                    amt_water_logged = min(l_val, r_val)
                    water_level = amt_water_logged - best_l_val
                    # print(water_level, width)
                    total_water += water_level * width

                    total_water -= best_l_val
                    best_l_val = l_val
                else:
                    total_water -= l_val

        return total_water


