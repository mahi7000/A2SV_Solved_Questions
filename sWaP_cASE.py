def swap_case(s):
    arr = list(s)
    
    for c in range(len(arr)):
        if arr[c].islower():
            arr[c] = arr[c].upper()
        else:
            arr[c] = arr[c].lower()
            
    return "".join(arr)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
