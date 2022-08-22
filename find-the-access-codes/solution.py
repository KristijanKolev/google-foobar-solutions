def solution(l):
    dynamo = []

    def dynamic_extend(num):
        l1 = 0
        l2 = 0
        for tup in dynamo:
            if tup[0] <= num and num % tup[0] == 0:
                l1 += 1
                l2 += tup[1]
        dynamo.append((num, l1, l2))

    for n in l:
        dynamic_extend(n)
    return sum([t[2] for t in dynamo])


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6]
    # from random import randint
    # test_list = [randint(1, 10**6) for _ in range(2000)]
    print(solution(test_list))
