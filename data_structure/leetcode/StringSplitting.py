class Solution(object):

    # Given a string s of zeros and ones, return the maximum score
    # after splitting the string into two non-empty substrings (i.e. left substring and right substring).
    #
    # Input: s = "011101", Output: 5
    # Explanation:
    # All possible ways of splitting s into two non-empty substrings are:
    # left = "0" and right = "11101", score = 1 + 4 = 5
    # left = "01" and right = "1101", score = 1 + 3 = 4
    # left = "011" and right = "101", score = 1 + 2 = 3
    # left = "0111" and right = "01", score = 1 + 1 = 2
    # left = "01110" and right = "1", score = 2 + 1 = 3
    def max_score(self, str):
        max_score = 0
        left_score = 0
        right_score = 0
        for c in str:
            if c == '1':
                right_score = right_score + 1
        for c in str:
            if c == '0':
                left_score = left_score + 1
            else:
                right_score = right_score - 1
            if max_score < left_score + right_score:
                max_score = left_score + right_score
        return max_score


if __name__ == '__main__':
    solution = Solution()
    print(solution.max_score("1111"))