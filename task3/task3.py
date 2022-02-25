# аргументы:  "-file_tests ./tests.json -file_values ./values.json"

import json
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Task 3')
    parser.add_argument("-file_tests", required=True,  help="tests.json var")
    parser.add_argument("-file_values", required=True,  help="values.json var")
    args = parser.parse_args()

    file_tests = args.file_tests
    file_values = args.file_values

    with open(file_tests, 'r', encoding='utf8') as f1:
        file1 = json.load(f1)

    with open(file_values, 'r', encoding='utf8') as f2:
        file2 = json.load(f2)


    def set_value(d):
        if not isinstance(d, dict):
            return d
        if d.get("value"):
            return d
        r = [x.get("value") for x in file2["values"] if x.get("id") == d.get("id")]
        if r and r[0]:
            d["value"] = r[0]
        return d


    def apply_recursive(func, obj):
        if isinstance(obj, list):
            return [apply_recursive(func, elem) for elem in obj]
        elif isinstance(obj, dict):
            obj = func(obj)
            return {k: apply_recursive(func, v) for k, v in obj.items()}
        else:
            return func(obj)


    _ = apply_recursive(set_value, file1)

    print(file1)

    with open('./report.json', 'w') as file:
        json.dump(file1, file, indent=3)
