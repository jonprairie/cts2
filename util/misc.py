def MultiDictInit(*args):
    '''extends dict.fromkeys syntax to allow for multiple
    key_list, value pairs'''
    ret_dict = dict()
    for arg in args:
        ret_dict.update(
            dict.fromkeys(
                arg[0],
                arg[1]
            )
        )
    return ret_dict
