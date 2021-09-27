import json


def conv_json(data_input):
    conv_json_data = json.dumps(data_input)
    return conv_json_data


new_dict = {
    "name": "Chuong",
    "class": "GCH16113",
    "age": 23
}
print(conv_json(new_dict))
