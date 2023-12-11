import math
if __name__ == '__main__':
    data = [1, 2, 100, -100, 10, 4, 30, 0, -25]
    result = sorted(data, key=abs)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: math.sqrt(x**2))
    print(result_with_lambda)
