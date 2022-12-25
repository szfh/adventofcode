import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = data_raw.splitlines()
    return data1


def snafu2dec(snafu: str) -> int:
    dec = 0
    for i, c in enumerate(snafu[::-1]):
        match c:
            case '2':
                dec += 2 * pow(5, i)
            case '1':
                dec += pow(5, i)
            case '0':
                dec += 0
            case '-':
                dec -= pow(5, i)
            case '=':
                dec -= 2 * pow(5, i)
    return dec


def dec2snafu(dec: int) -> str:
    snafu = []
    while dec > 0:
        dec, divisor = divmod(dec, 5)
        if divisor >= 3:
            dec += 1
            divisor -= 5
        snafu.append('=-012'[divisor + 2])
    return ''.join(snafu[::-1])


def part1(data):
    data_dec = []
    [data_dec.append(snafu2dec(x)) for x in data]
    return dec2snafu(sum(data_dec))


def main():
    file = os.path.abspath("../../data/2022/day25.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %s' % part1(data))


if __name__ == "__main__":
    main()
