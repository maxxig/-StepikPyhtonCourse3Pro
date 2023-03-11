def matrix_by_elem(matrix):
    # for m in matrix:
    #     for s in m:
    #         yield s
    yield from (s for m in matrix for s in m)


matrix = [[1, 2, 3, 5, 6, 7, 8],
          [9, 10, 11, 12, 13, 14, 15]]

print(list(matrix_by_elem(matrix)))