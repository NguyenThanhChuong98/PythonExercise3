import json


def unique_key(data_input):
    conv_json = json.loads(data_input)
    return conv_json


new_obj = '{"a":1,"a":2,"a":3,"a":4,"b":2,"b":2,"c":3,"d":4}'
print(unique_key(new_obj))
