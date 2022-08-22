def solution(n, b):
    def str_base(number, base):
        (d, m) = divmod(number, base)
        if d > 0:
            return str_base(d, base) + str(m)
        return str(m)

    def str_base_filled(number, base, length):
        base = str_base(number, base)
        zeros_fill = '0' * (length - len(base))
        return zeros_fill + base

    sequence = [n]
    while True:
        last_num = sequence[-1]
        n1 = "".join(sorted(last_num, reverse=True))
        n2 = "".join(sorted(last_num))
        res_int = int(n1, b) - int(n2, b)
        res = str_base_filled(res_int, b, len(n))
        try:
            loop_start = sequence.index(res)
            return len(sequence) - loop_start
        except ValueError:
            sequence.append(res)
            continue


if __name__ == '__main__':
    print solution('210022', 3)


