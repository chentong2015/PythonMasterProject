
def test_list():
    shop_list = ['apple', 'mango', 'carrot']
    print('I have', len(shop_list), 'items')
    for item in shop_list:
        print(item)
    shop_list.append('rice')


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


def test_set():
    # create an empty set
    empty_set = set()
    empty_set.add("item1")
    empty_set.add("item2")
    print("Set values: ", empty_set)




