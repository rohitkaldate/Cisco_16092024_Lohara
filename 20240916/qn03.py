number_list= list(map(int,input("Enter at least 5 integers: ").split()))

number_tuple= tuple(number_list)
number_set= set(number_list)

number_frozen= frozenset(number_set)
number_dict = {num: num ** 2 for num in number_set}


print(f"Original list: {number_list}")
print(f"Converted to tuple: {number_tuple}")
print(f"Original set: {number_set}")
print(f"Frozen Set: {number_frozen}")
print(f"Dictionary numbers: {number_dict}")

import json

with open('qn03_data.json','w') as number_db:
    json.dump(number_dict,number_db)
print("Dictionary written to JSON file.")

with open('qn03_data.json','r') as number_db:
    number_dict2= json.load(number_db)
    print(f'Reading json file....\n{number_dict2}')
    