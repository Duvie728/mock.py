##from datetime import datetime
##now = datetime.now()
##date = now.strftime("%x")
##time = now.strftime("%I:%M %p")
##
##print("welcome {} and {}".format(date,time))
####print(" {} , {}".format(date,time))
##print("welcome  Elizabeth,today is {} and  it is {}".format(date,time))

def convert_hex_to_symbol(hex_string: str) -> chr:
    return chr(int(hex_string, 16))
# call it
naira_symbol = convert_hex_to_symbol("20A6")
