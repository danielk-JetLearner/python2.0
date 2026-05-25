def hour_to_min(hour):
    min = (hour*60)
    return min
while True:
    print("1. convert hour to minute")
    print("2. convert minute to hour")
    print("3. exit")
    choice = int(input("what do you want to do"))
    if choice == 1:
        
        taco = int(input("Enter time in hours"))
        tuesday = hour_to_min(taco)
        print(tuesday)
        
        