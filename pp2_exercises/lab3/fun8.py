def spy_game(nums):
    c=False
    for i in range(0,len(nums)-1):
        if(nums[i]==0):
            for j in range(i+1,len(nums)):
                if(nums[j]==0):
                    for x in range(j+1,len(nums)):
                        if(nums[x]==7):
                            c=True
    print(c)