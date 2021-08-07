# to print prime numbers till given value
def prime(n):
    for x in range(2, n//2+1):
        if n% x==0:
            return 0
        return 1


n=int(input("Enter the range value: "))
primes=[]
i=2
while len(primes)<n:
    if prime(i)==1:
        primes.append(i)
    i=i+1
print("The first",n , "prime numbers are", primes)

#thanks for watching
#like, share & subscribe to,
# Dream2code
