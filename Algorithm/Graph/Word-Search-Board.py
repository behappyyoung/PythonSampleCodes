"""
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0

"""
def find_word(word, x, y, board):
    word_length = len(word)
    if word_length <=1:
        return True

    c_index = 1
    c_word = word[c_index]
    b_max = len(board[0])
    c_x = x -1 if x > 0 else x + 1
    c_y = y
    while c_index < word_length:
        found = False
        if board[c_x][c_y] == c_word:
            found = True
        if x > 0:
            if not found:
                c_x = x - 1
            if board[c_x][c_y] == c_word:
                found = True


        if found:
            c_index += 1
            c_word = word[c_index]


def wordExist(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == B[0]:
                if find_word(B, i, j, A):
                    return 1
    return 0
