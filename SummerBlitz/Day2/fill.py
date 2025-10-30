from sre_parse import WHITESPACE


row = []

for i in range(8):
    row.append(WHITESPACE)

squares = [x ** 2 for x in range(10)]

odds = [x for x in squares if x % 2 != 0 ]

board = [[EMPTY for i in range(8)] for j in range(8)]

