#Kadane's Algorithm is used to find the continuous subarray in the One-Dimensional integer array, which has the largest sum possible.

def max_Subarray_Sum(my_array, array_size):  
  
    maxTillNow = my_array[0]  
    maxEnding = 0  
      
    
    for n in range(0, array_size):  
        maxEnding = maxEnding + my_array[n]  
        
        if maxEnding < 0:  
            maxEnding = 0  
          
        elif (maxTillNow < maxEnding):  
            maxTillNow = maxEnding  
              
    return maxTillNow  
 
my_array = [-2, -3, 4, -1, -2, 5, -3]  
  
print("Maximum Subarray Sum:", max_Subarray_Sum(my_array, len(my_array)))  
