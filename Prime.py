def is_prime(num):
    if num <= 1:
        print("numbers lesser than 2 are not prime numbers.") 
        return
    if num == 2:
        print("2 is a prime number")
        return
    
    is_not_prime = False
    for i in range(2,int(num/2)+1,1):
        if num%i == 0:
            is_not_prime = True
            break

    if is_not_prime:
        print("not a prime")
    else:
        print("is a prime")

is_prime(1)
is_prime(2)
is_prime(-1)
is_prime(9)
    