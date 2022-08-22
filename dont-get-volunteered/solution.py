def solution(src, dest):
    from collections import namedtuple
    Field = namedtuple('Field', 'x y')
    BOARD_SIZE = 8

    def get_coords(order_number):
        x = int(order_number / BOARD_SIZE)
        y = order_number % BOARD_SIZE
        return Field(x, y)

    def search_neighbours(cur_field, cur_steps):
        if cur_field == dest_field:
            board[dest_field.x][dest_field.y] = min(board[dest_field.x][dest_field.y], cur_steps)
        elif cur_steps < board[cur_field.x][cur_field.y]:
            board[cur_field.x][cur_field.y] = cur_steps
            for field in get_neighbours(cur_field):
                search_neighbours(field, cur_steps + 1)

    def get_neighbours(field):
        neighbours = []
        for t in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            n = Field(field.x + t[0], field.y + t[1])
            if n.x in range(BOARD_SIZE) and n.y in range(BOARD_SIZE):
                neighbours.append(n)
        return neighbours

    board = [[10 ** 10 for i in range(8)] for j in range(8)]
    src_field = get_coords(src)
    dest_field = get_coords(dest)

    search_neighbours(src_field, 0)
    return board[dest_field.x][dest_field.y]


if __name__ == '__main__':
    print(solution(19, 36))
