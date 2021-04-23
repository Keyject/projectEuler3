# KeyJect
# Euler 3
import math
def isPrime(num):
  for i in range(2 , int(math.sqrt(num))+1):
    if num%i==0:
      return False
  return True

# num = 13195 
num = 600851475143 
for i in range(2 , num):
  if num%i==0:
    temp = num/i
    if isPrime(temp):
      print(temp)
      break