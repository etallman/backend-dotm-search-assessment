print('Imported my_module...')

# test = 'Test String'

def find_pricing(to_search, optional_dir):
    '''Find the documents containing a '$' character to find out where pricing info is stored.'''
    for i, value in enumerate(to_search):
        if value == optional_dir:
            return i
    return -1

#####Flags
#python dotm_search.py --dir ./dotm_files "$" 
#python dotm_search.py "other text"