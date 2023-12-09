First thought, we can use trees again here!!
Write bt tree code (binary tree)
BUUTTT
the code doesn't seem to be fitting or a tree.
more just pointers
hmmm but it might work. let me try

trees sux. too hard

hahahaha solved part 1 using dictionaries

but part 2.. too long


new game plan:
1. assumption: each sequence will eventually repeat
2. if it repeats, we can fomulate an equation for the repetition
3. solve when they will repeat and match

problem 1:
how to find if pattern repeats.
references:
https://www.geeksforgeeks.org/find-recurring-sequence-fraction/?ref=header_search
https://www.geeksforgeeks.org/longest-repeating-and-non-overlapping-substring/?ref=header_search

eureka moment: in the decimal/fraction solution, they stored in a map the remainders. if the remainder is in the map, we have entered a loop.

we can also use the same idea for the problem.
store in a map the node value AND the direction to go to. if we go somewhere again, its a loop!!
fucking smart.
lets go~

FUCK REPEATER CODE WORKED
WOO LETS FUCKING GOOOOOOO

welp
tried in production code.
i forgot to factor in the input.
so is that another curve
fucking curve
I HATE THIS
the repeating is not true because the input will also change

unless ....

there is a point where it will repeat with the same input?
whew
will run it and see what happens


o m g
there is!!!
whewwwww

ALSO
there is exactly one Z for each starting node.
meaning.. it can really be modeled via a cosine/sine wave.
periodicity is every time we get the answer

saving this here

NODE0: 0LDPA
final: 0LNGZ
period 20780
answer: 20777

NODE1: 0LQLA
final: 0LXMZ
period 19204
answer: 19199

NODE2: 0LVJA
final: 0LGLZ
period 18677
answer: 18673

NODE3: 0LGTA
final: 0LFXZ
period 16045
answer: 16043

NODE4: 0LAAA
final: 0LZZZ
period 12365
answer: 12361

NODE5: 0LXQA
final: 0LHHZ
period 15519
answer: 15517

getting the waves:
\sin\left(\frac{2\pi x}{2\cdot20777}\right)
sin ((2pi*x)/ (2* ANSWER)) - confirmed in desmos


hmmm rather than solving math, what if iterate na lang?
increase the numbers until mag same. faster yun kesa x + 1 ganon

okay, coded the iteration and increase.
even with this new algo, ang tagal??
parang ang taas ng number hahahahaha
feel ko faster pa rin. hindi +1 yung increment
at the time of writing, first algo (bruteforce) is 28100000000
tapos nasa 332835260793 na yung 2nd algo. and wala pa rin
for context:
28100000000
332835260793

tapos wala pa rin yung solution. hahahahaha depota ang saya

why do i have a feeling na pag minultiply ko yung 6 numbers yun yung answer

so minultiply ko, eto yung number
22920415997392119919569089
10000000000000000000000000
hahahahahahahahhahahahahahhahahaha gl mabruteforce

try ko nga sa day 8

okay too high raw, buti naman

FUCK
triny ko
10000000000000000000000000, too low raw. gago matagal pa to hahahaha
1140863054631 pa lang

shet may naisip akong bagong algo.
multiply factors to 2 numbers until maging same yung 2, tapos divide sa other numbers. if walang remainder, yun na yun.
better ata than accumulator, try ko nga

okay may multiplying algo na ko
current value ng 2nd algo
3429095252896
10000000000000000000000000
malayo pa hahahahaha

omg ang bilis ng 3rd algo.
2742366119852 agad after 2 mins. compared sa other
3429095252896
4117126335091 after 4 mins!!! omg hahahaha
1000000000000
10000000000000000000000000
dapat ata naglagay ako ng seed number para mas mabilis

okay. so nagquick maths ako.
takes me around 8 mins to get ~10000000000000 results
13 na ganon para mareach yung minimum. so 1 hour 44 mins para lang ma reach
hahanapin pa yung sagot, so times 2 non. 3 hours 28 mins siguro.
hahahah tagal ampota. gawin ko na yung seeding

okay try ko rnning with the seed. 10000000000000 / 20777 = 48130143.9091
48130143 para efas. g

okay ligo muna brb

2453207811365
10000000000000

mali math ko.
4.81301439091 e+20 dapat
481301439091000000000 <- eto seed


okay, umabot ako dito
10000000000004538236719014
too high raw. hmmmmmmm
may mali ba sa algo ko

so in between
10000000000000000000000000
10000000000004538236719014

trying to debug, codify na rin nung ibang manually ko inextract
4.813014390914954e+20 new seed
481301439091495400000
10000000000004000000000000 from this


hmmm same answer pa rin sakin
10000000000004538236719014 - steps
481301439091521308982 - multiplier to 20777

tried to sanity test this the minimum
10000000000000000000000000 pero di na gumagana. wala nang too high or too low :(

okay 2nd algo finished with a low value: 18215611419223



fuck yeah it worked. baka periodic din yung intersections nila?
so mali siguro yung naenter ko na nagsabi na too low?
18215611419223
10000000000000 - baka eto pala yung too low. makes sense kasi tignan mo o

anyway, on to the next one. I won't even clean this up HAHAHAHAHA

running tests* kasi di ako masyadong conviced
876719999 yung multiplier using algo 3. try ko irun

shet nag 0 nga. pota hahahahahhaa
18215611419223 yung periodicity nung perfect thing
36431222838446

okay chapter closed na nga hahaha

