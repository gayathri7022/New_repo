def is_prime(num):
    if num <= 1:
        return False
        
    if num == 2:
        return True
    
    is__prime = True
    for i in range(2,int(num/2)+1,1):
        if num%i == 0:
            is__prime = False
            break

    if is__prime:
        return True
    else:
        return False
print(is_prime(8))
    