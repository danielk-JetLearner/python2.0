try:

    hmmmmmmmm = int (input("write a number(if your sister is annoying type either 6, 7, or 8)"))
    mysisterisannoying =int(input("write a second number(is your big sister is annoying type either 11, 12, or 13)"))
    try: 
        supercalifragilisticexpialidocius = (hmmmmmmmm/mysisterisannoying)
        print(supercalifragilisticexpialidocius)
    except ZeroDivisionError:
        print("cannot divide by zero")
except ValueError:
    print ("cannot divide letters")
