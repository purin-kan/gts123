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


def Ticketprice(seatType, movieType):
    if seatType in ['p', 'P']:
        if movieType == 1:
            return 100
        elif movieType == 2:
            return 120
    elif seatType in ['d', 'D']:
        if movieType == 1:
            return 140
        elif movieType == 2:
            return 200
    elif seatType in ['h', 'H']:
        if movieType == 1:
            return 400
        elif movieType == 2:
            return 500


globalSeatType = ''
globalMovieType = 0

seatType()
Movietype()

print("The ticket price is %s" % Ticketprice(globalSeatType, globalMovieType))
