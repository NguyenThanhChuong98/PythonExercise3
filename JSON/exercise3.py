import json


def convert_json(data_input):
    conv_json = json.dumps(data_input)
    return conv_json


new_dict = {"Power": 100, "Energy": 200, "Speed": 300}
print(convert_json(new_dict))
