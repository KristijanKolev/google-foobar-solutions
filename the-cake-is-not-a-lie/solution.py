def solution(s):
    for piece_len in range(1, len(s)/2 + 1):
        if len(s) % piece_len != 0:
            continue
        piece = s[0:piece_len]
        num_pieces = len(s) / piece_len
        if piece * num_pieces == s:
            return num_pieces
    return 1


if __name__ == '__main__':
    print solution("abcabcabcabc")
