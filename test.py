def series_sum(n):
    sum = 0
    if n == 1:
        return format(float(n), ",.2f")
    for i in range(1, n * 3 + 1, 3):
        sum += 1 / i
    return format(float(sum), ",.2f")

    # Happy Coding ^_^

print(series_sum(2))

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

def longest(s1, s2):
    if len(s1)>len(s2):
        return "".join((sorted(set(s1))))
    return "".join((sorted(set(s2))))


def binaryToNumber(array):
    return str(int(str("".join(array)), 2))  # your code

print(int("".join([str(x) for x in [1, 0, 0, 1]]), 2))

print("".join(str([1, 2, 3, 4])))