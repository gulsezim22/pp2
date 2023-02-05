def has_33(nums):
    n=len(nums)-1
    solution=False
    for i in range(0,n):
        if(nums[i]==3 and nums[i+1]==3):
            solution=True
    print(solution)