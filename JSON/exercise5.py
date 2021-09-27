import json


def conv_python_obj(data_input):
    conv_obj = json.loads(data_input)
    return conv_obj


new_dict = '{"Power": 100, "Energy": 200, "Speed": 100}'
print(conv_python_obj(new_dict))
