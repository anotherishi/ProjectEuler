# def is_triangular(number: int):
#     x = (-1 + (1 + 8 * number) ** .5) / 2
#     return x == int(x)

# def is_pentagonal(number: int):
#     x = (1 + (1 + 24 * number) ** .5) / 6
#     return x == int(x)

# def is_hexagonal(number: int):
#     x = (1 + (1 + 8 * number) ** .5) / 4
#     return x == int(x)

# i = 1
# # while True:
# #     if is_triangular(i) and is_pentagonal(i) and is_hexagonal(i):
# #         print(' \n\n\n\n\n\n                      ', i, '\n\n\n\n')
# #     i += 1

# print(is_triangular(14191127))





from math import sqrt

i = 0
while True:
    i += 1
    a = (i * (i + 1)) / 2
    b = (1 + sqrt(1 + 24 * a)) / 6
    c = (1 + sqrt(1 + 8 * a)) / 4
    if (b % 1) == 0.0:
        if (c % 1) == 0.0:
            print( a)
            if a > 40755:
                break
