input_string = input('Enter a String: ')
l = 0
for i in input_string:
    print(input_string[(len(input_string)- l)-1],end = '') #found out how to do end = '' on stackoverflow, everything else is mine
    #https://stackoverflow.com/questions/12032214/print-new-output-on-same-line (source)
    l += 1