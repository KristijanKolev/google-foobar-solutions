def solution_slow(n):
    from math import log

    number = int(n)
    cache = {}
    min_steps = [10 ** 300]  # list because mutable object is needed

    def is_power_of_two(num):
        return (num & (num - 1) == 0) and num != 0

    def recursive_step(current_num, current_steps):
        if current_steps >= min_steps[0]:
            return
        cached_steps = cache.get(current_num, None)
        if cached_steps is not None and cached_steps <= current_steps:
            return
        if is_power_of_two(current_num):
            min_steps[0] = min(min_steps[0], current_steps + log(current_num, 2))
            return

        if current_num % 2 == 0:
            recursive_step(current_num / 2, current_steps + 1)
        else:
            recursive_step(current_num + 1, current_steps + 1)
            recursive_step(current_num - 1, current_steps + 1)

    recursive_step(number, 0)
    return int(min_steps[0])


def solution_wrong(n):
    number = int(n)
    power = 0
    while True:
        p1 = 2**power
        if p1 >= number:
            p0 = 2**(power - 1)
            d1 = p1 - number
            d0 = number - p0
            if d1 < d0:
                return d1 + power
            else:
                return d0 + power - 1
        power += 1


def solution_new(n):
    import sys
    sys.setrecursionlimit(2000)
    number = int(n)
    MAX_INT = 10**300
    cache = {
        1: MAX_INT
    }

    def recursive_step(current_num, current_steps):
        if cache[1] <= current_steps or current_num < 1 or cache.get(current_num, MAX_INT) <= current_steps:
            pass
        else:
            cache[current_num] = current_steps
            if current_num % 2 == 0:
                recursive_step(current_num / 2, current_steps + 1)
            else:
                recursive_step(current_num + 1, current_steps + 1)
                recursive_step(current_num - 1, current_steps + 1)

    recursive_step(number, 0)
    return int(cache[1])


if __name__ == '__main__':
    num_str = '9' * 200
    print(num_str)
    print(solution_new(num_str))