def romantoarabic(user_input):
    '''dict of critical roman values created '''
    ls = {'IV': 4, 'IX': 9,
          'XL': 40, 'XC': 90,
          'CD': 400, 'CM': 900,
          'I': 1, 'V': 5,
          'X': 10, 'L': 50,
          'C': 100, 'D': 500,
          'M': 1000}

    '''just to make the search process easier these two lists are defined'''
    search_list1 = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    search_list2 = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    sum1 = 0
    sum2 = 0
    for i in range(0, len(user_input)):
        if user_input[i:i + 2] in search_list1:
            found = user_input[i:i + 2]
            sum1 += ls.get(found)
        else:
            if user_input[i - 1:i + 1] in search_list1:
                continue
            elif user_input[i] in search_list2:
                f = user_input[i]
                sum2 += ls.get(f)

    return sum1 + sum2

