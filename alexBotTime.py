import time

def getEorzeaTime():
    eConst = 20.571428571428573
    eEpoch = int(time.time() * eConst)
    days = eEpoch/86400 # num days since 1970/01/01

    ddiff = days - int(days)
    etHours = (int(ddiff * 24))
    mdiff = (ddiff*24 - etHours)
    etMins = int(mdiff * 60)
    return str("{0:0=2d}".format(etHours)) + ':' + str("{0:0=2d}".format(etMins))


def nodeFinder():
    results = 'Currently available nodes: \n'
    test = getEorzeaTime().replace(':', '')
    tempTime = int(test)

    if tempTime >= 0 and tempTime <= 155:
        results += 'Ala Mhigan Salt Crystal (21,28) nearest to Porta Praetoria [until 13:55] \n'
        results += (155-tempTime)*3 + 'seconds left \n \n'
    
    if tempTime >= 1200 and tempTime <= 1355:
        results += 'Ala Mhigan Salt Crystal (21,28) nearest to Porta Praetoria [until 13:55] \n'
        results += (1355-tempTime)*3 + 'seconds left \n \n'
    
    return results
