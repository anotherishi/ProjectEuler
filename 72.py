from math import gcd


def solution(input_d: int = 10e6) -> int:

    result = 0

    # loop through all the possible fractions for a given value of 'input_d'
    for numerator in range(1, input_d):
        for denominator in range(numerator + 1, input_d + 1):
            # count only if the fractions are reduced
            if gcd(numerator, denominator) == 1:
                result += 1

    return result


if __name__ == "__main__":
    print(f"{solution() = }")
