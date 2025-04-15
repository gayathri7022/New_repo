from Prime import is_prime

def Test_cases():
    assert(is_prime(1)) == False
    assert(is_prime(2)) == True
    assert(is_prime(-1)) == False
    assert(is_prime(9)) == True

Test_cases()

