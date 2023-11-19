# TODO. 对于list列表，直接遍历其中所有元素或者使用index来定位元素
def test_list():
    shop_list = ['apple', 'mango', 'carrot']
    print('I have', len(shop_list), 'items')
    for item in shop_list:
        print(item)
    for index in range(len(shop_list)):
        print(shop_list[index])
    shop_list.append('rice')
    shop_list.sort()  # 直接调用排序方法


# 二维list数组也是相同的操作方式，调用相应的API
def test_list_with_2_dimension():
    return_types = [["a", "b"], ["c", "d"]]
    print("---")
    return_types.append(["e", "f"])
    print(len(return_types))
    print(return_types.pop(0))


def test_set():
    # create an empty set
    empty_set = set()
    empty_set.add("item1")
    empty_set.add("item2")
    print("Set values: ", empty_set)


# 字典是存储<key, value>的数据结构
def test_dictionary():
    # create an empty dictionary
    empty_dictionary = {}

    key_values = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    print(key_values['key1'])
    del key_values['key2']
    print(len(key_values))


def test_dic(x, y, operator):
    x = int(x)
    y = int(y)
    result = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }
    print("Result = ",  result.get(operator, 0))



