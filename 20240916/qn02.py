names_list= input("Enter student names: ").split()
names_set= set(names_list)
names_first= frozenset(names_set)
names_dict= {name:len(name) for name in names_first}

print(f"Original list: {names_list}")
print(f"Set(no duplicate): {names_set}")
print(f"Frozen set: {names_first}")
print(f"Dictionary of name length: {names_dict}")

import json
with open('qn02_data.json','w') as names_db:
    json.dump(names_dict,names_db)
print("Dictionary written to json file.")

with open('qn02_data.json','r') as names_db:
    names_dict2 = json.load(names_db)
    print(f'Reading  JSON file....\n{names_dict2}')
    
    