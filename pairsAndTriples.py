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

# lambda sum for reduce --------------------------------
myTotal = lambda x, y: x + y

if __name__ == "__main__":
    MY_TEXT_FILE = open("C:/Users/Mikaela/Documents/Spring2020/CS441 Progrm LangDes&Imp/Final Project/testFile2.txt",
                        "r")
    FILE_STRING = MY_TEXT_FILE.read()

    startClock = time.perf_counter_ns()  # EXCLUDE FILE I/O FOR THE TIMER --------------------------

    # use SET to grab uniques
    MY_UNIQUES_TUPLE = set(x for x in FILE_STRING)  # USED FOR SINGLES
    # need to pass PAIRS and TRIPLES to count new values for NC -- instead of count char, count pairs
    # [line[i:i+n] for i in range(0, len(line), n)] where n = 2
    MY_PAIRS_TUPLE = set(FILE_STRING[i: i+2] for i in range(0, len(FILE_STRING), 2))  # USED FOR PAIRS
    MY_TRIPLES_TUPLE = set(FILE_STRING[i: i+3] for i in range(0, len(FILE_STRING), 3))  # USED FOR TRIPLES
    # CONSIDER FILE_STRING.UPPER() OR FILE_STRING.LOWER() to reduce load
    # print(MY_UNIQUES_TUPLE)  # CAN CHECK SET OF ALL UNIQUE CHARS HERE IF YOU WANT

    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_UNIQUES_TUPLE)  # COUNTS SINGLES
    # print(tuple(NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS))
    NUMBER_OF_TIMES_EACH_PAIR_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_PAIRS_TUPLE)
    # print(tuple(NUMBER_OF_TIMES_EACH_PAIR_OCCURS))
    NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_TRIPLES_TUPLE)
    # print(tuple(NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS))
    MY_TOTAL_CHARACTERS = reduce(myTotal, NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS)  # SPENT ITERATOR
    print("TOTAL NUMBER OF CHARACTERS: " + str(MY_TOTAL_CHARACTERS) + " (used to solve for pc)")

    # iterator is spent to build MY_TOTAL_CHARACTERS, need to remake
    # reset iterator
    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_UNIQUES_TUPLE)

    MY_PROBABILITIES_OF_EACH_CHARACTER = map(lambda x: round(x/MY_TOTAL_CHARACTERS, 3),
                                             NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS)  # SPENT ITERATOR AGAIN
    MY_PROBABILITIES_OF_EACH_PAIR = map(lambda x: round(x/MY_TOTAL_CHARACTERS, 3),
                                        NUMBER_OF_TIMES_EACH_PAIR_OCCURS)  # SPENT
    MY_PROBABILITIES_OF_EACH_TRIPLE = map(lambda x: round(x/MY_TOTAL_CHARACTERS, 3),
                                          NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS)  # SPENT

    # PROBABILITY DISTRIBUTIONS
    print("PROBABILITY DISTRIBUTION: " + str(tuple(MY_PROBABILITIES_OF_EACH_CHARACTER)) + " (single characters)")
    print("PROBABILITY DISTRIBUTION: " + str(tuple(MY_PROBABILITIES_OF_EACH_PAIR)) + " (pairs)")
    print("PROBABILITY DISTRIBUTION: " + str(tuple(MY_PROBABILITIES_OF_EACH_TRIPLE)) + " (triples)")

    # reset BOTH iterators FOR ALL
    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_UNIQUES_TUPLE)
    MY_PROBABILITIES_OF_EACH_CHARACTER = map(lambda x: round(x / MY_TOTAL_CHARACTERS, 3),
                                             NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS)  # SPENT AGAIN

    NUMBER_OF_TIMES_EACH_PAIR_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_PAIRS_TUPLE)
    MY_PROBABILITIES_OF_EACH_PAIR = map(lambda x: round(x / MY_TOTAL_CHARACTERS, 3),
                                        NUMBER_OF_TIMES_EACH_PAIR_OCCURS)  # SPENT

    NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_TRIPLES_TUPLE)
    MY_PROBABILITIES_OF_EACH_TRIPLE = map(lambda x: round(x / MY_TOTAL_CHARACTERS, 3),
                                          NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS)  # SPENT

    # RESET NC AGAIN
    NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_UNIQUES_TUPLE)
    NUMBER_OF_TIMES_EACH_PAIR_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_PAIRS_TUPLE)
    NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS = map((lambda x: FILE_STRING.count(x)), MY_TRIPLES_TUPLE)

    # map this function: (nc)(−pc)lg(pc) to each NC
    MY_INFORMATION_OF_EACH_CHARACTER = map((lambda nc, pc: round(nc * (-pc) * math.log(pc, 2), 3)),
                                           NUMBER_OF_TIMES_EACH_CHARACTER_C_OCCURS,
                                           MY_PROBABILITIES_OF_EACH_CHARACTER)
    MY_INFORMATION_OF_EACH_PAIR = map((lambda nc, pc: round(nc * (-pc) * math.log(pc, 2), 3)),
                                      NUMBER_OF_TIMES_EACH_PAIR_OCCURS,
                                      MY_PROBABILITIES_OF_EACH_PAIR)
    MY_INFORMATION_OF_EACH_TRIPLE = map((lambda nc, pc: round(nc * (-pc) * math.log(pc, 2), 3)),
                                        NUMBER_OF_TIMES_EACH_TRIPLE_OCCURS,
                                        MY_PROBABILITIES_OF_EACH_TRIPLE)

    # get the summation
    MY_TOTAL_INFORMATION_IN_STREAM = round(reduce(myTotal, MY_INFORMATION_OF_EACH_CHARACTER), 3)
    MY_TOTAL_INFORMATION_PAIRS = round(reduce(myTotal, MY_INFORMATION_OF_EACH_PAIR), 3)
    MY_TOTAL_INFORMATION_TRIPLES = round(reduce(myTotal, MY_INFORMATION_OF_EACH_TRIPLE), 3)

    RUN_TIME = ((time.perf_counter_ns()) - startClock)  # END TIME - START TIME to get duration
    print(str(RUN_TIME) + " nanoseconds")
    print(str(RUN_TIME / 1000) + " microseconds (μs)")
    print(str(RUN_TIME / 1000000000) + " seconds")  # to return seconds
    # 2 decimals w/ str(round(answer, 2))
    print(str(round(RUN_TIME / 1000000000, 2)) + " seconds (rounded)")

    # TOTAL INFORMATION IN THE FILE
    print("INFORMATION IN DATA STREAM: " + str(MY_TOTAL_INFORMATION_IN_STREAM) + " (SINGLES)")
    print("INFORMATION IN DATA STREAM: " + str(MY_TOTAL_INFORMATION_PAIRS) + " (PAIRS)")
    print("INFORMATION IN DATA STREAM: " + str(MY_TOTAL_INFORMATION_TRIPLES) + " (TRIPLES)")
