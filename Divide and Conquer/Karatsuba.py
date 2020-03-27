def karatsuba(num1,num2):
    """
    Function to perform Karatsuba Multiplication:
    suppose num1 = 1234,num2 = 4567
    a = 12
    b = 34
    c = 45
    d = 67

    num1 * num2 = ac * 10 ** (n//2) + ((ad+bc) * 10 ** (n/2)) + bd

    """
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1 * num2
    
    n = max(len(str(num1)), len(str(num2)))
    nby2 = n // 2
    ten_pow_nby2 = 10**nby2
    a = num1 // ten_pow_nby2
    b = num1 % ten_pow_nby2
    c = num2 // ten_pow_nby2
    d = num2 % ten_pow_nby2

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # this little trick, writing n as 2*nby2 takes care of both even and odd n
    prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

    return prod
