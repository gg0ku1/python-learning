arr = [5, 3, 4, 1, 2]

n = len(arr)
mid = n // 2

left = arr[:mid]
right = arr[mid:] #slicing

left_n = len(left)
left_mid = left_n // 2

left_l = left[:left_mid]
left_r  = left[left_mid:]

right_n = len(right)
right_mid = right_n // 2

right_l = right[:right_mid]
right_r  = right[right_mid:]

right_r_n = len(right_r)
right_r_mid = right_r_n // 2

right_r_l = right_r[:right_r_mid]
right_r_r  = right_r[right_r_mid:]

#base case reached

