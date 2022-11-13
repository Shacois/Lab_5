from pprint import pprint

list_dicts = [{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(16)]
pprint(list_dicts)
