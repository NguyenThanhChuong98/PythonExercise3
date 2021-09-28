import json


def check_compl(data_input):
    if '__complex__' in data_input:
        return complex(data_input['real'], data_input['img'])
    return data_input


complex_object = json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook=check_compl)
print(complex_object)
