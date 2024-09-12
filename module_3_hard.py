data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(lst):
    global_sum = 0
    if isinstance(lst, (list)):
        for i in lst:
            if isinstance(i, (int, float)):
                global_sum += i
            elif isinstance(i, (str)):
                global_sum += len(i)
            elif isinstance(i, (list)):
                for item in i:
                    if isinstance(item, (int, float)):
                        global_sum += item
                    elif isinstance(item, (str)):
                        global_sum += len(item)
            elif isinstance(i, (dict)):
                lst1 = i.keys()
                lst2 = i.values()
                for item in lst1:
                    if isinstance(item, (int, float)):
                        global_sum += item
                    elif isinstance(item, (str)):
                        global_sum += len(item)
                for item in lst2:
                    if isinstance(item, (int, float)):
                        global_sum += item
                    elif isinstance(item, (str)):
                        global_sum += len(item)
            elif isinstance(i, (tuple)):
                for item in i:
                    if isinstance(item, (int, float)):
                        global_sum += item
                    elif isinstance(item, (str)):
                        global_sum += len(i)
                    elif isinstance(item, (dict)):
                        global_sum += calculate_structure_sum([item])

    return global_sum
result = calculate_structure_sum(data_structure)
print(result)
