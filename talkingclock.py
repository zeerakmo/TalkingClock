import sys
import re

def talkClock(time):
    x=time.split(":")
    mydict = {
        1:"Ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        2:"Twenty",
        3:"Thirty",
        4:"Fourty",
        5:"Fifty"
    }
    hours = ["twelve","one","two","three","four","five","six","seven","eight","nine","ten","eleven"]
    day = hours[int(x[0])%12]

    if (int(x[1])) ==0:
        past_to=""
    elif (int(x[1])) > 30:
        x[1]=str(60-int(x[1])).zfill(2)
        day = hours[(int(x[0])+1)%12]
        past_to = " to "
    elif (int(x[1]))<30:
        past_to = " past "
    else:
        past_to = "Half past "
        mins = ""
        print(mins,past_to,day ,sep="") 
        return

    minutes = [int(x[1][0]),int(x[1][1])]
    if (minutes[1] == 0):
        if (minutes[0] == 0):
            mins=""
            day = day.capitalize()+" o'clock"
        else:
            mins = mydict[minutes[0]]
    elif (minutes[0] == 1):
        mins = mydict[int(x[1])].capitalize()
    elif (minutes[0] == 0):
        mins = hours[minutes[1]].capitalize()
    else:
        mins= mydict[minutes[0]].capitalize()+" "+hours[minutes[1]]

    print(mins,past_to,day, sep="")
    return 

def main():

    if ( len(sys.argv)) ==1:
        print("No Argument given")
        return
        
    if ( len(sys.argv)) >2:
        print("Too Many Arguments given")
        return

    pattern = re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
    
    if (pattern.match(sys.argv[1])) == None:
        print("Invalid format")
        return
    else:
        talkClock(str(sys.argv[1]))


if __name__ == "__main__":
    main()


