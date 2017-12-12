def get_even_list(l):
    even_numbers = []
    for i in l:
        if i%2 == 0:
            even_numbers.append(i)
    return even_numbers
