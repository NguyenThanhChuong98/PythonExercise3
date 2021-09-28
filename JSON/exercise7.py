import json


def check_ins(data_input):
    if isinstance(data_input, complex):
        return [data_input.real, data_input.imag]
    else:
        return False


check_complex = json.dumps(2 + 3j, default=check_ins)
print(check_complex)
