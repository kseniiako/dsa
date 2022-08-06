

def englishRuler(length, ticks):
    """ Print out an English ruler """
    if length < 0:
        print("Length of ruler must be >=0")
        return
    for x in range(length+1):
        print(tickshelper(ticks) + " " + str(x))
        if x != length:
            rulerhelper(ticks)

def tickshelper(ticks):
        return ("-")*ticks

def rulerhelper(ticks):
    if ticks == 2:
        print(tickshelper(1))
    if ticks > 2:
        rulerhelper(ticks-1)
        print(tickshelper(ticks-1))
        rulerhelper(ticks-1)

if __name__ == "__main__" :
    englishRuler(2, 4)
    englishRuler(7, 3)
    englishRuler(0, 8)
    englishRuler(-1, 8)