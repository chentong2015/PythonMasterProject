class Solution(object):
    """
    Given two strings needle and haystack,
    return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        :type haystack: str
        :type needle: str
        :rtype: int
    """

    # TODO. 字符串的操作方式如同list一样，可以根据index来获取char
    def test_full_string(self, full_string):
        print(len(full_string))
        for c in full_string:
            print(c)
        for i in range(len(full_string)):
            print(full_string[i])

    def index_of_sub_string(self, full_string, sub_string):
        if len(sub_string) > len(full_string):
            return -1
        for i in range(len(full_string)):
            found_index = True
            for j in range(len(sub_string)):
                if full_string[i + j] != sub_string[j]:
                    found_index = False
                    break
            if found_index:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.index_of_sub_string("kbsadbutsad", "sad"))
