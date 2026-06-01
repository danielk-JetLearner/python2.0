def hour_to_min(hour):
    our = (hour*60)
    return our

def min_to_hour(mins):
    min = (mins/60)
    return min
while True:
    print("1. convert hour to minute")
    print("2. convert minute to hour")
    print("3. exit")
    choice = int(input("what do you want to do? "))
    if choice == 1:
        
        taco = int(input("Enter time in hours: "))
        tuesday = hour_to_min(taco)
        print(tuesday)
    if choice == 2:
        wave = int(input("Enter time in minutes, *60: "))
        wednesday = min_to_hour(wave)
        print(wednesday)
    if choice == 3:
        break
            
        
        
        
            

        
        