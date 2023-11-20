# Written by Po

def seatType():
    while True:
        seattype = input("Select the seat type (P or D or H): ")
        if seattype in ['P', 'D', 'H']:
            global globalSeatType
            globalSeatType = seattype
            break
        else:
            print("Wrong seat type! Please select")


def Movietype():
    while True:
        movietype = input("Select the movie type (1 or 2): ")
        if movietype in ["1", "2"]:
            global globalMovieType
            globalMovieType = int(movietype)
            break
        else:
            print("Wrong movie type! Please select again.")


def Ticketprice():
    global globalSeatType
    global globalMovieType
    
    if globalSeatType in ['p', 'P']:
        if globalMovieType == 1:
            return 100
        elif globalMovieType == 2:
            return 120
    elif globalSeatType in ['d', 'D']:
        if globalMovieType == 1:
            return 140
        elif globalMovieType == 2:
            return 200
    elif globalSeatType in ['h', 'H']:
        if globalMovieType == 1:
            return 400
        elif globalMovieType == 2:
            return 500


globalSeatType = ''
globalMovieType = 0

seatType()
Movietype()

print("The ticket price is %s" % Ticketprice())
