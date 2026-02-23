# Creating a Dictionary
dict1 = {'key1':'Sam', 'key2':999, 5:'Mark'}
dict1['key1'] # 'Sam'
dict1[5] # 'Mark'
type(dict1) # dict - shows type of argument (data type)
dict1.keys() # dict_keys(['key1', 'key2', '5'])
dict1.values() # dict_values(['Sam', 999, 'Mark'])
dict1.items() # dict_items([('key1':'Sam'), ('key2':999), (5:'Mark')])
type(dict1.items()) # dict_items