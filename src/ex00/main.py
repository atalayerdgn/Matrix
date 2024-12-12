from _00 import Solution

def main():
	matrix1 = [[1, 2], [3, 4]]
	matrix2 = [[5, 6], [7, 8]]
	s = Solution(matrix1)
	s._add(matrix2)
	print(s.reshape())
	s._sub(matrix2)
	print(s.reshape())
	s.scl(2)
	print(s.reshape())	

if __name__ == "__main__":
	main()
