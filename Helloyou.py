import time

a = True
while a == True:
    hello = "Hello you, mijn naam is {owner}. En hoe heet jij?"
    print(hello.format(owner = "Senno Taphoorn"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hello " + username)

    time.sleep (10)
    
    break
