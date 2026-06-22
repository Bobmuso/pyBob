full_dot = '●'
empty_dot = '○'

def create_character(name, st, iq, char):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif  not isinstance(st, int) or not isinstance(iq, int) or not isinstance(char, int):
        return "All stats should be integers"
    elif st < 1 or iq < 1 or char < 1 :
        return "All stats should be no less than 1"
    elif st > 4 or iq > 4 or char > 4 :
        return "All stats should be no more than 4"
    elif st + iq + char != 7:
        return "The character should start with 7 points"

    return f"{name}\nSTR {(st * full_dot) + ((10 - st) * empty_dot)}\nINT {(iq * full_dot) + ((10 - iq) * empty_dot)}\nCHA {(char * full_dot) + ((10 - char) * empty_dot)}"
