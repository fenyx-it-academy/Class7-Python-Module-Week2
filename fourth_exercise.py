def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
def is_prime(num):
    for i in range(2,num):
        if (num%i) == 0:
            return False
    return True

def nearest_palindromical_prime_number(num_1, num_2, num_3):
    mul = num_1 * num_2 * num_3

    for number in range(mul, 0, -1):
        if is_palindrome(number):
            if is_prime(number):
                return number


    return None


p_prime_num = nearest_palindromical_prime_number(31, 77, 99)
print(p_prime_num)

