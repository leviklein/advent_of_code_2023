okay, mukhang magagamit graphs ulit dito.
or not?

conditions that I see:
. is a separator
each ? is a node
multiple contiguous # is one node
every ? has 2 outcomes, either . or #

what if we just generate each and then get the ones that match the groupings?
2^n permutations, where n = number of ?

okay gumana yugn said implementation sa part 1.
bale gumamit ako bitoperations
    0 == .
    1 == #
tapos ginagawa kong int.
mini optimization ay minemakesure ko yung count ng # ay equal para dun sa number na tinetest
pero masyado pa ring matagal for this problem

need ko ng better checker kesa iteration
smart enough to handle the pattern


HMMM what if we convert this to a purely bitwise problem?
group all the dots to be 1 dot.

???.###????.###????.###????.###????.###
1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3


hmmm while thinking about this naisip ko. what if magstart tayo backwards? from answer to possible combinations?
