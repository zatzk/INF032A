nums = []
i=0

while i < 15:
     nums.insert(i, input("Digite o numero: "))  
     i+=1
i=0    
while i < len(nums):
     x = nums[i]
     print("numero {}: {}".format(i, nums[i]))
     if(int(x)%2) == 0:
     	print("par\n")
     else:
     	print("impar\n")
     i+=1

