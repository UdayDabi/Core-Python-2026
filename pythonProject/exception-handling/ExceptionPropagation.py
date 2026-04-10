def son():
    # yaha exception throw ho raha hai
    raise RuntimeError("make a mistake")


def mom():
    # yaha handle nahi ho raha → propagate hoga
    son()


def dad():
    try:
        mom()   # call ho raha hai
    except RuntimeError as e:
        print(e)   # yaha handle ho gaya


# main function jaisa
dad()