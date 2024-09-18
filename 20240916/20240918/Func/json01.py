import json
patients= [
    {'id': 101, 'name': 'raj'}, 
    {'id': 102, 'name': 'rushi'}, 
    {'id': 103, 'name': 'dravid'}
] 

patients_str = json.dumps(patients)
print(patients,patients_str)

with open ('patients_data.json','w') as patients_db:
    json.dump(patients,patients_db)
    
patients_list2 = json.loads(patients_str)
print(patients_list2, type(patients_list2))

with open('patients_data.json','r') as patients_db:
    patients_list3 = json.load(patients_db)
    print(patients_list3, type(patients_list3))
