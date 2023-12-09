okayyyy
mukhang pascal's triangle pero subtract tapos hindi nagsstart sa 1
triangles hehehe
unang thought, create lahat ng layers. pero baka mas efficient kunin yung first few elements tapos kunin yung last. lets see

try ko muna non-efficient way

wait di ko need gumawa ng triangles! kunin ko lang yung 2 elements nung line tapos subtract then add. check ko if gagana



omg it's not workiiiiing hahahahahahhahahahahahahaha why

issue in first entry:
1 element na lang tapos hindi pa 0.
how to handle

first handling,
    # curr_row = [-93024]
    # next_row = []
    if len[next_row] = 0:
        next_row = [curr_row[0], curr_row[0]]
    # next_row = [-93024, -93024]

answer1 1878654470 - too high raw

try ko 2nd handling,
    if len[next_row] = 0:
        next_row = [0]

answer 1866957968 - too high pa rin damnit


okay looking at the inputs.
merong cases na nag-eend sa isang number na non zero


OKAY so nag nap ako tapos tapos na ni denise. sabi nya baka raw di ko nahahandle negative numbers. at tama siya HAHAHAHAHA