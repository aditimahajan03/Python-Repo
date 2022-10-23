command =""
# we will input value for multiple options thats
# why we have an empty string
repeat = False
while True:
    command = input(">").lower()
    if command == "start":
        if repeat:
            print("Car has already started")
        else:
            repeat = True
            print("car started")
    elif command == "stop":
        if repeat:
            print("car has already stopped")
        else:
            repeat = True
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command =="quit":
        break
    else:
        print("i don't understand that")
# dry = Don't Repeat Yourself
