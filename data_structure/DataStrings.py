
def test_data_string():
    single_q = 'this is a string'
    double_q = "this is a string"
    print(single_q, double_q)

    # 将字符串切割之后，形成的是字符串数组，相同的遍历方式
    full_string = "a b ac cd"
    strs = full_string.split(' ')
    print(len(strs))
    print(strs[0])


if __name__ == '__main__':
    test_data_string()