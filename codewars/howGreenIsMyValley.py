

def find_highest(arr):
    high = { 'index': 0, 'value': arr[0] }
    for i in range(1, len(arr)):
        if arr[i] > high['value']:
            high['index'] = i 
            high['value'] = arr[i]
    
    new_arr = arr[0: high['index']] + arr[high['index'] + 1:]
    return { 'high': high['value'], 'new_arr': new_arr }
    

def make_valley(arr):
    '''
    How Green is my Valley
    The problem is worded weird, but essentially you
    are building a valley. Basically you find the
    highest points, and build from the top down.
    The first highest is the left, the second highest
    is the right and it alternates.
    '''
    left = []
    right = []
    go_left = True
    go_right = False

    
    while len(arr):
        high = find_highest(arr)
        arr = high['new_arr']

        if go_left:
            left.append(high['high'])
            go_left = False 
            go_right = True
        elif go_right:
            right = [high['high']] + right
            go_left = True 
            go_right = False

    return left + right


print(make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]))