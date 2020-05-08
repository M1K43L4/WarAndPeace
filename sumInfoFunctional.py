import time
import math
from functools import reduce

'''
REQUIREMENTS FOR: COUNTING THE TOTAL NUMBER OF CHARACTERS
* know count of each unique (ALREADY DONE)
* return sum of these counts

PROBABILITY DISTRIBUTION:
* probability p of some character c (pc) is the NUMBER OF OCCURRENCES OF C divided by TOTAL CHARACTERS IN DATA STREAM
** so pc = nc / total c
* probability distribution is the probability of EACH CHARACTER in data stream
'''

'''
REQUIREMENTS FOR: A FUNCTIONAL PARADIGM
* need to use map/reduce
* functional paradigms use CONSTANTS outside their scope; doesn't rely on mutable variables -- passes returned results
* from function to function 
** PURE functional programs only depend on their input (no internal state)
'''
# lambda sum for reduce
myTotal = lambda x, y: x + y


if __name__ == "__main__":
    startClock = time.perf_counter_ns()
    MY_TEXT_FILE = open("C:/Users/Mikaela/Documents/Spring2020/CS441 Progrm LangDes&Imp/Final Project/testFile2.txt",
                        "r")
    FILE_STRING = MY_TEXT_FILE.read()

    # my generator expressions
    CHARACTER_COUNTER = (FILE_STRING.count(x) for x in FILE_STRING)
    CHARACTER_PRINTER = (x for x in FILE_STRING)
    # print(tuple(CHARACTER_COUNTER))  # returns a tuple of the counts of EVERY character -> shows duplicates
    # print(tuple(CHARACTER_PRINTER))  # returns EVERY character -> shows duplicates
    # my dictionary expression
    MY_DICTIONARY_COUNTS_OF_CHARACTERS = dict([(x, FILE_STRING.count(x)) for x in FILE_STRING])
    # print(MY_DICTIONARY_COUNTS_OF_CHARACTERS)  # returns EACH character -> no duplicates - ONLY UNIQUES!!
    # NUMBER_OF_UNIQUES = len(MY_DICTIONARY_COUNTS_OF_CHARACTERS)
    # print(NUMBER_OF_UNIQUES)
    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: MY_DICTIONARY_COUNTS_OF_CHARACTERS.get(x)),
                                                  MY_DICTIONARY_COUNTS_OF_CHARACTERS)

    MY_TOTAL_CHARACTERS = FILE_STRING.__len__()

    MY_PROBABILITIES_OF_EACH_CHARACTER = map(lambda x: round(x/MY_TOTAL_CHARACTERS, 3),
                                             NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS)  # PROBABILITY DISTRIBUTION
    # iterator is spent, need to remake
    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: MY_DICTIONARY_COUNTS_OF_CHARACTERS.get(x)),
                                                  MY_DICTIONARY_COUNTS_OF_CHARACTERS)

    # map this function: (nc)(−pc)lg(pc) to each NC
    MY_INFORMATION_OF_EACH_CHARACTER = map((lambda nc, pc: round(nc * (-pc) * math.log(pc, 2), 3)),
                                           NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS,
                                           MY_PROBABILITIES_OF_EACH_CHARACTER)
    MY_TOTAL_INFORMATION_IN_STREAM = round(reduce(myTotal, MY_INFORMATION_OF_EACH_CHARACTER), 3)
    print(MY_TOTAL_INFORMATION_IN_STREAM)  # TOTAL INFORMATION IN THE FILE

    RUN_TIME = ((time.perf_counter_ns()) - startClock)  # end time - start time to get duration
    print(str(RUN_TIME) + " nanoseconds")
    print(str(RUN_TIME / 1000) + " microseconds (μs)")
    print(str(RUN_TIME / 1000000000) + " seconds")  # to return seconds
    # 2 decimals w/ str(round(answer, 2))
    print(str(round(RUN_TIME / 1000000000, 2)) + " seconds (rounded)")
