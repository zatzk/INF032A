nums = []
i=0

while i < 8:
     nums.insert(i, input("Digite o numero: "))  
     i+=1
i=0    
while i < len(nums):
     x = nums[i]
     y = 2
     print("numero {}: {}".format(i, nums[i]))
  
     for y in range (20):
     	  if(int(x)) == 6*y:
     	  	print("multiplo de 6")
     	  	y+=1
     	
     i+=1

