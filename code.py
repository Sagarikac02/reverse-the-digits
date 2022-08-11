n = int(input())
rev = n%10
n = n//10
while(n > 0):
  r = n % 10
  n = n//10
  rev = rev*10 + r
print(rev)
