def number_pattern(n):

    if not isinstance(n, int) :
        return "Argument must be an integer value."
    
    elif n < 1 :
        return "Argument must be an integer greater than 0."
    pattern = ""
    
    for i in range(n):
        pattern += str(i + 1) + " "
    
    return pattern.strip()
    
print(number_pattern(12))