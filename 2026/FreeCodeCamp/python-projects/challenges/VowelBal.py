#challenge 11 Aug 25 done on 6/24/25 for 25th 


def is_balanced(s):
    mid1 = ""
    mid2 = ""
    
    half = len(s) //2
 
    if len(s) % 2 == 0 :
        
        mid1 = s[:half ]
        mid2 = s[half:]
    else:
        mid1 = s[:half + 1 ]
        mid2 = s[half:]
        
    half1 = 0 
    half2 = 0
    
    for i in range(len(mid1)):
        if mid1[i].lower() in "aeiou":
            half1 += 1
            
            
    for j in range(len(mid2)):
        if mid2[j].lower() in "aeiou":
            half2 += 1
    
            
    if half1 == half2:
        return True, mid1, mid2, half1, half2
    elif half1 != half2:
        return False
   


is_balanced("Kitty Ipsum")