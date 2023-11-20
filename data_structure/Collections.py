# 在一个函数体内使用yield表达式会使这个函数变成一个生成器函数
def do(collection, predicate):
    for item in collection:
        if predicate(item):
            yield item


def test_collection(collection, predicate):
    result = [item for item in collection if predicate(item)]
    result = (item for item in collection if predicate(item))
    return result

