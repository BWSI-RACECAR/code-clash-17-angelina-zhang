"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #17 - Pascal's Triangle (pascal.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Blaise Pascal is a famous French Mathematician and Philosopher who 
created Pascal's Triangle. Pascal's Triangle is a triangular array composed of 
binomial coefficients that arises in probability theory, combinatorics, and algebra. (Wikipedia)

Prompt: Given the number of rows, return a 2D list of Pascal's Triangle

Test Cases:
Input: rows = 1 ; Output = [[1]]
Input: rows = 2 ; Output = [[1], [1, 1]]
Input: rows = 3 ; Output = [[1], [1, 1], [1, 2, 1]]

"""

class Solution:
    def pascalTri(self,rows):
        # type row: int
        # return type: list[list[int]]

        # TODO: Write code below to return a nested list with the solution to the prompt
        # list_all = []
        # old_list = []
        # count_j = 0
        # for i in range(0, rows):
        #     new_list = []
        #     new_list.append(1)
        #     if old_list is not None:
        #         for j in range (2, i-2):
        #             new_j = old_list[j-1] + old_list[j]
        #             new_list.append(new_j)
        #             count_j = j
        #         if count_j >1:
        #             new_list.append(1)
        #             old_list = new_list
        #     list_all.append(new_list)
            
        # return list_all
        tri = [[1]]
        for _ in range(rows):
            tri.append([x+y for x,y in zip(tri[-1] + [0],[0]+ tri[-1])])
        return tri[:rows]

def main():
    num = int(input())

    tc1 = Solution()
    ans = tc1.pascalTri(num)
    print(ans)

if __name__ == "__main__":
    main()