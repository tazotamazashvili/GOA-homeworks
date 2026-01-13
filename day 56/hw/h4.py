def ragac(sia):
    luwebi = [x for x in sia if x % 2 == 0]
    kentebi = [x for x in sia if x % 2 != 0]
    return luwebi + kentebi