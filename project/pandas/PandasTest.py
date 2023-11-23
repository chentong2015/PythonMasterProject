import pandas as pd
import csv


if __name__ == '__main__':
    data = pd.read_csv("D:/test/input.csv", encoding="utf-8", dtype=object)
    print(data["name"].dtypes)
    print(data["name"])

