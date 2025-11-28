class pair_elements():

    def twoSum(self,nums,target):
        #create an empty dictionary
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num]=i

#taking input from the user
value = int(input("Enter the number for which you want to make a search: "))
print("Index1 = %d, Index1 = %d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))