def fill_char(*args):
    if len(args)==2:
        return fill_char1(args[0], args[1])
    elif len(args)==3:
        return fill_char1(args[0], args[1], args[2])
    elif len(args)==1:
        return fill_char2(args[0])

def fill_char1(char, width, type = "I"):
    if (type=="F"):
        x = str(format(char, ".3f"))
    else:
        x = str(char)
    x = x[:width].rjust(width, " ")
    return x

def fill_char2(char_format):
    tmp_text = ""
    for x in char_format:
        if len(x)>2:
            tmp_text += fill_char1(x[0], x[1], x[2])
        else:
            tmp_text += fill_char1(x[0], x[1])
    return tmp_text

def rounding(number):
    return str(format(number, ".3f"))

print(fill_char(63897.12739, 10))