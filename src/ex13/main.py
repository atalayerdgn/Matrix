from _13 import Solution


def main():
    # Example Usage
    u1 = [
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ]
    
    u2 = [[1., 2., 0., 0.],[2., 4., 0., 0.],[-1., 2., 1., 1.]]
    
    u3 = [
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.]
    ]
    
    solver = Solution()
    print(solver.rank(u1))  # Output: 3
    print(solver.rank(u2))  # Output: 2
    print(solver.rank(u3))  # Output: 4 (or depending on the matrix's actual rank)
    

if __name__ == '__main__':
    main()
