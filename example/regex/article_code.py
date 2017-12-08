#!/usr/bin/env python3
"""
Example of function using regex on lists.
"""
import re
#line = "barbary, froufrou, mathematic, damnably, corundum, pouchlike"

do = ['09/10', '05-2010', '07-20', '10/1999']
dont = ['001-11', '10.15', '01/115', '13-2001']
patt = r"^(0[1-9]|1[0-2])(\/|-)([0-9]{4}|[0-9]{2})$"


def regex_on_list(should_match, shouldnt_match, patter, index=0):
    """
    Function for using regex search function on a
    list that contains string that should match
    and a list with string that shouldnt match.
    """
    print(should_match, shouldnt_match)
    should = []
    shouldnt = []
    for word in should_match:
        should.append(re.search(patter, word).group(index))
    for word in shouldnt_match:
        result = re.search(patter, word)
        if result:
            shouldnt.append(result.group(index))
    print(dir(re))
    if shouldnt:
        should.append(shouldnt)
    return should

#print(regexOnList(do, dont, patt))

#line = "Ross McFluff: 0456-45324: 155 Elm Street\n\
#   Ronald Heathmore: 5543-23464: 445 Finley Avenue"

line = "https://dbwebb.se/kunskap/uml#sequence,\
        ftp://bth.com:32/files/im.jpeg,\
        file://localhost:8585/zipit, http://v2-dbwebb.se/do%hack"

match = re.findall(r"(\w+)://([\w\-\.]+).(\d+)?", line)
print(str(match))


# inte:[jja), (fdskf}, {fsfk] ja:kök], {fjldf}, (flkdsf)
