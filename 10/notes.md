first thought, wow this is a maze generation and solving problem.
maybe there's a library na tutulungan ako?
pero grabe yung nakita ko. tutorial!!
thanks internet!
link: https://realpython.com/python-maze-solver/

okay nacode ko na yung solution. gumana sa test_input. pero I have problems in mind:
nakabase ako na yung maximum loop == loop na andun yung S. feeling ko sa input na to hindi eh.

okay bago matulog nacode ko yung condition na maximum loop that includes the entrance. pero nagccrash kasi kinocompute niya lahat. need ko magawan ng way na magsimula siya sa S (entrance)

okay so I tried doing something. cycle_basis instead of simple_cycles.
first answer tried:
125 - too low raw

okay svg is now working. nice
napagana ko rin yung walls (ground == wall)
pero
yung ibang nodes na di na accessible (dahil nafill yung borders from adjacent cells) ay naccount pa rin. need to make a function to handle those

offending nodes
Square(index=1010, row=7, column=30, border=<Border.LEFT|TOP: 5>, role=<Role.NONE: 0>),
Square(index=1011, row=7, column=31, border=<Border.LEFT|TOP: 5>, role=<Role.NONE: 0>),
Square(index=1012, row=7, column=32, border=<Border.LEFT|TOP: 5>, role=<Role.NONE: 0>)


okay nasolve ko na ata yung offending nodes.
tried to run pero eto sagot
max_length: 8627
answer1: 4313.5 - tried 4134 pero too low pa rin
hmm AHHH siguro dahil hindi counted yung empty spaces. nodes lang yun


okay I tried using nx.path_weight
this yielded
max_length: 13661.0
answer1: 6830.5 - tried to submit 6831 pero too low pa rin hmmmmm


6831 <- Tried this again PERO TAMA NA. WTF ANO BA YAN HAHAHAHHAHAHAHAHAHAH
