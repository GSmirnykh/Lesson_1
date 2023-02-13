def get_summ(one, two, delimiter='&'):
    return str(one) + str(delimiter) + str(two)

func = get_summ('Learn', 'python')
print(func.upper())
