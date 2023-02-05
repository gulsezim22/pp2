def solve(numheads, numlegs):
    rabbit_count=(numlegs-2*numheads)/2
    chicken_count=numheads-rabbit_count
    print(int(chicken_count),int(rabbit_count))