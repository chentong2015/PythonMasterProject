from typing import List


# 验证数度9*9的数据是否有效
# 1. 验证每一个Row的数据是否有效
# 2. 验证每一个Col的数据是否有效
# 3. 验证每一个3*3的方格是否有效
def check_sudoku(sudoku: List[List[int]]) -> str:
    for row in range(9):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for col in range(9):
            for index in range(9):
                if soduku[row][col] == nums[index]:
                    nums[index] = 0
        for index in range(9):
            if nums[index] != 0:
                return "LINE " + str(row) + " INVALID"

    for col in range(9):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(9):
            for index in range(9):
                if soduku[row][col] == nums[index]:
                    nums[index] = 0
        for index in range(9):
            if nums[index] != 0:
                return "COLUMN " + str(col) + " INVALID"

    return "foo"


if __name__ == '__main__':
    soduku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    print(check_sudoku(soduku))
