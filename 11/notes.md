first idea, wow magagamit ko ata natutunan ko last time HAHA

pero parang mas madali

di pala ako nakapagnotes pero tapos ko na part1.
!!!
10313550

medyo matagal processing, estimate ko 1 hour pero parang 30 mins ata not sure.

pero sure ako na gusto ko ioptimize.
multiprocessing based sa yt vid na nakita ko.
need lang icheck if:
1. better ba to save graph to file then load for each process
2. or just copy the whole graph
3. input batch size for each process? I think dependent to sa first 2. if gano katagal yung instantiation time. if total time = processing time + instantiation time, siguro yung good metric is processing time > 100* instantiation time

pero di ko muna to iccode. life muna ;)


for part2, instead of adding 1 more line, add 1,000,000 more

okay optimization muna, pag isipan ko yung part 2 after maoptimize.

so for first testing:
multiprocessing with function of g being passed. not sure if better yung iload ko from file, try ko later.
with g being passed somehow (access from global namespace),
most efficient yung chunksize of 1. tested with 10, and 1000, bumagal.


additional rows = 1

input = 36 items
chunksize   | time (s)
1           | 0.0167
1000        | 0.0187

input = 101926 items
chunksize   | time (s)
1           | 308.8961s
100         | 299.0021s
1000        | 309.6752s
5000        |




HAHAHAHAHA TANGINA MAY REALIZATION AKO
DI MO NEED MAG GRAPHS FOR A CARTESIAN PLANE
NEED MO LANG YUNG COMPUTE YUNG DIFFERENCE IN INDICES DEPOTA HAHAHAHAHAHAHAHAHAHA


okay 14/12/2023, gagwin ko na ulit

okay EZ hahaha tangina mo jepoy dizon
you had me in the first half, not gonna lie
