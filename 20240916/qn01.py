# accepting input from user:

user_input= input("Enter list of words: ")
words_list= user_input.split()

print("List of words:",words_list)


#convert list into tuple: 

words_tuple= tuple(words_list)

print(words_tuple)

with open('qn01_data.txt','w') as data_file:
    data_file.write(f'List:{words_list}')
    data_file.write(f'Tuple:{words_tuple}')
print("Data written to file")

with open('qn01_data.txt','r') as data_file:
    line_list= data_file.readline()
    line_tuple= data_file.readline()
    
    print(line_list)
    print(line_tuple)
    