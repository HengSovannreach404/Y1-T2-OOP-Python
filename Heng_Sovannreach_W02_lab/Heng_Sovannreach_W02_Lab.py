'''
------------------
    Exercise 1
------------------
'''
print('Exercise 1')
def reverse(mylist):
    size = len(mylist)
    half_size = int(size / 2)
    for i in range(half_size):
        temp = mylist[i]
        mylist[i] = mylist[size - i - 1]
        mylist[size - i - 1] = temp
    return mylist

mylist = [1,2,3,4,5]
print("Reversed: ", reverse(mylist))

'''
------------------
    Exercise 2
------------------
'''
print('Exercise 2')
squares = [i**2 for i in range(1, 21) if i % 2 == 0]
print(squares)


'''
------------------
    Exercise 3
------------------
'''
print('Exercise 3')
def merge(list1, list2):
    merge_list = list1 + list2
    union_list = []
    for i in range(int(len(merge_list))):
        if merge_list[i] not in union_list:
            union_list.append(merge_list[i])
    return union_list

list1 = [1,2,3]
list2 = [2,3,4,5]

print(merge(list1, list2))

'''
------------------
    Exercise 4
------------------
'''
print('Exercise 4')
def get_min(tuple_num):
    min = tuple_num[0]
    for i in range(len(tuple_num)):
        if tuple_num[i] < min:
            min = tuple_num[i]
    return min

def get_max(tuple_num):
    max = tuple_num[0]
    for i in range(len(tuple_num)):
        if tuple_num[i] > max:
            max = tuple_num[i]
    return max

def max_min(tuple_num):
    return (get_max(tuple_num), get_min(tuple_num))

tuple_num = (10,5,8,12,3)

print(max_min(tuple_num))  

'''
------------------
    Exercise 5
------------------
'''
print('Exercise 5')
GPS = (('Phnom Penh', 11.5564, 104.9282),
        ('Siem Reap', 13.3622, 103.8597), 
        ('Battambang', 13.0957, 103.2022))


for slot in range(len(GPS)):
    i = 0
    print(f'City: {GPS[slot][i]}, Latitude: {GPS[slot][i + 1]}, Longitude: {GPS[slot][i + 2]}')


'''
------------------
    Exercise 6
------------------
'''
print('Exercise 6')
dicts = {1: 10, 2: 20, 3: 30, 4: 40}

value_list = list(dicts.values())
double_value = lambda x : x * 2

for i in range(len(value_list)):
    dicts.update({i + 1 : double_value(value_list[i])})

print(dicts)

'''
------------------
    Exercise 7
------------------
'''
print('Exercise 7')
def frequency(string):
    char_list = []
    for i in range(len(string)):
        char_list.append(string[i])

    dicts = {}
    for i in char_list:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    return dicts

string = 'hello'
print(frequency(string))

'''
------------------
    Exercise 8
------------------
'''
print('Exercise 8')
def merge_dicts(dicts_1, dicts_2):
    new_dicts = {}
    new_dicts.update(dicts_1)
    new_dicts.update(dicts_2)
    
    common = dicts_1.keys() & dicts_2.keys()

    if len(common) > 0:
        for i in common:
            new_dicts[i] = dicts_1[i] + dicts_2[i]

    return new_dicts

dicts_1 = {'a': 1, 'b': 2}
dicts_2 = {'b': 3, 'c': 4}

print(merge_dicts(dicts_1, dicts_2))