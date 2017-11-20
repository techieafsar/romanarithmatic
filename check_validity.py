def roman_validity(number):
    '''a list of commonly invalid roman values is created '''
    invalid_list = ['IIII', 'XXXX', 'CCCC', 'MMMM', 'VV', 'LL', 'DD', 'VX', 'DM', 'LC', 'IM', 'XD', 'XM']
    if '0' in number:
        raise ValueError(' input {} is invalid '.format(number))
    for i in invalid_list:
        if i in number:
            raise ValueError(' input {} is invalid '.format(number))

