def group_list_product(custom_list, size=1):
    group_list = []
    group_size = size
    my_range = range(0, len(custom_list), group_size)
    for i in my_range:
        group_list.append(custom_list[i:i + group_size])
    return group_list