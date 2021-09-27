import json


def convert_python_object(data_input):
    conv_py_obj = json.loads(data_input)
    return conv_py_obj


new_json = '{ "Name":"Chuong", "Class":"GCH16113", "Age":23 }'
print(convert_python_object(new_json))
