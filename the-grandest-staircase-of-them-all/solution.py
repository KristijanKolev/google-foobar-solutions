def solution(n):
    import math

    memos = {}
    def get_combos(bricks, start_height):
        if bricks / 2.0 <= start_height:
            return 0
        if (bricks, start_height) in memos:
            return memos[(bricks, start_height)]
        total_combos = 0
        for i in range(start_height, int(math.ceil(bricks / 2.0))):
            sub_combos = get_combos(bricks - i, i + 1)
            total_combos += 1 + sub_combos
        memos[(bricks, start_height)] = total_combos
        return total_combos

    return get_combos(n, 1)


if __name__ == '__main__':
    print(solution(200))
