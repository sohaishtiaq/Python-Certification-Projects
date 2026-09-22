def square_root_bisection(num, tol= 0.01, max_iter = 100):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if num == 0 or num ==1:
        print(f"The square root of {num} is {num}")
        return num

    low = 0
    high = max(1, num)
    for _ in range(max_iter):
        mid = (low + high) / 2
        if high - low <= tol:
            print(f"The square root of {num} is approximately {mid}")
            return mid 

        if mid * mid < num:
            low = mid
        else:
            high = mid 
    print(f"Failed to converge within {max_iter} iterations")
