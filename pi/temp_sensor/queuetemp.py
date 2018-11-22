import readxbee


PERIOD = 5
def getval():
    try:
        val = int(readxbee.get_voltage())
        print("Got Value:",val)
        return val
    except KeyboardInterrupt:
        exit()
    except:
        return getval()
q = []
while len(q) < 11:
    q.append(getval())

growingcount = 0
droppingcount = 0
oqpied = False

#currentval = getval()
#change = 0

while True:
    currentval = getval()
    if (growingcount >= 10):
        oqpied = True
        growingcount = 0
        droppingcount = 0
    elif droppingcount >=10:
        oqpied = False
        droppingcount = 0
        growingcount = 0
    else:
        change = currentval - q[0]
        if change >= PERIOD:
            growingcount += 1
            droppingcount = max(droppingcount - 1, 0)
        elif change <= -PERIOD/2:
            droppingcount += 1
            growingcount = max(growingcount - 1, 0)
        else:
            growingcount = max(growingcount - 1, 0)
            droppingcount = max(growingcount -1, 0)
    del q[0]
    q.append(currentval)
    #currentval=getval()
    print("Queue={}, Growing={}, Dropping={}, Occupied={}, Change={}".format(q,growingcount,droppingcount,oqpied,change))
    #lastval = currentval
    #currentval = getval()
