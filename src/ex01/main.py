from _01 import Solution

def main():
	matrix1 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
	matrix2 = [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
	solution = Solution(matrix1, matrix2)
	solution.linear_combination(2, -1)
	result = solution.reshape()
	print("Result:")
	for row in result:
	    print(row)
if __name__ == "__main__":
	main()
