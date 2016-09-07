

#Create a dictionary
heap = [(-f, c) for c, f in collections.Counter(str).items()]


#Create multu demension array
dp = [[0 for x in range(len(nums))] for y in range(len(nums))]
