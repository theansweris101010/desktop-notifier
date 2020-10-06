def getWorkHours():    
    while True:
        try:
            startDay = int(input("From 1 to 23, What time do you start your day?" ))
            endDay = int(input("From 1 to 23, What time do you end your day?" ))
            if startDay > 23 or endDay > 23:
                raise Exception("Error! This is not a valid hour. Try again")

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        # When successfully converted to an integer,
        # the loop will end.
        else:
            break
    return startDay, endDay