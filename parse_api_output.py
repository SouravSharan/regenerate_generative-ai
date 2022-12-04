import json
from datetime import datetime

def parse_timeline():
    txt = open('timeline.txt').readlines()
    #print(txt)
    ret = {'dates' : [], 'events' : []}
    for k in txt:
        k = k.strip("\n")
        if k == "":
            continue
        #print()
        d = k.split("–")[0].split('.')[1]
        e = k.split("–")[1]

        #d = format_date(d)

        ret['dates'].append(d)
        ret['events'].append(e)
        #print(ret)
    return ret

#parse_timeline()