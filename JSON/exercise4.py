import json


def conv_json(data_input):
    sort_dict = dict(sorted(data_input.items(), key=lambda item: item[0]))
    conv_json_data = json.dumps(sort_dict, indent=4)
    return conv_json_data


new_dict = {"A": 10, "b": 20, "C": 35, "d": 21, "E": 22}
print(conv_json(new_dict))
