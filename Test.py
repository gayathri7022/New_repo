from Prime import is_prime

def Test_cases():
    assert is_prime(1) == "numbers lesser than 2 are not prime numbers."
    assert is_prime(2) == "2 is a prime number"
    assert is_prime(-1) == "numbers lesser than 2 are not prime numbers."
    assert is_prime(9) == "not a prime"