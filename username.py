while True:
    user=input ("what is your full name?")
    print(user.split())
    name=user.split()
    if user.lower()=='exit':
        break
    
    if len(name)<2:
        continue