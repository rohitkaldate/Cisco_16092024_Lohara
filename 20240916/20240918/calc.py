def find_diff(first:int=1, second:int=0)->int:
    return first - second

print(find_diff(20,10)) #10
print(find_diff(second= 10, first= 20)) #10  (20-10)

print(find_diff(second=10)) #-9  (1-10)
print(find_diff())#1  (1-0)
