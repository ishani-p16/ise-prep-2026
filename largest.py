largest=None
for nums in [23,-3,100,101,-34]:
    if largest is None or nums>largest:
        largest=nums
    print('loop:',nums,largest)
print('largest:',largest)
print('YIPPEE TASK IS DONE')