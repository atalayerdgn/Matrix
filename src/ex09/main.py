from _09 import Solution


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix:
        print(row)
    sol = Solution()
    print("-------------------------")
    for row in sol.transpose(matrix):
        print(row)

if __name__ == '__main__':
    main()
