import time
'''
REQUIREMENTS FOR: COUNTING THE OCCURRENCES OF EACH CHARACTER
* know what each character is (in the file) (MAY NOT BE NECESSARY)
* be able to return a count of each of those characters (REDUCE SHOULD DO THIS; it returns a single value)
** start by being able to return the count of a chosen character
# example: how many a's are in my file? REDUCE should return this
** now be able to return the count of ANY character
# example: how many 'INPUT_VALUE' are in my file?

'''

'''
REQUIREMENTS FOR: A FUNCTIONAL PARADIGM
* need to use map/reduce
* functional paradigms use CONSTANTS outside their scope; 
* PURE functional programs only depend on their input (no internal state)
'''

if __name__ == "__main__":
    startClock = time.perf_counter_ns()
    MY_TEXT_FILE = open("C:/Users/Mikaela/Documents/Spring2020/CS441 Progrm LangDes&Imp/Final Project/testFile2.txt",
                        "r")
    FILE_STRING = MY_TEXT_FILE.read()
    myFileIterator = iter(FILE_STRING)

    # my generator expressions
    CHARACTER_COUNTER = (FILE_STRING.count(x) for x in FILE_STRING)
    CHARACTER_PRINTER = (x for x in FILE_STRING)
    print(tuple(CHARACTER_COUNTER))  # returns a tuple of the counts of EVERY character -> shows duplicates
    print(tuple(CHARACTER_PRINTER))  # returns EVERY character -> shows duplicates
    # my dictionary expression
    MY_DICTIONARY = {(x, FILE_STRING.count(x)) for x in FILE_STRING}
    print(MY_DICTIONARY)  # returns EACH character -> no duplicates - ONLY UNIQUES!!

    RUN_TIME = ((time.perf_counter_ns()) - startClock)  # end time - start time to get duration
    print(str(RUN_TIME) + " nanoseconds")
    print(str(RUN_TIME / 1000) + " microseconds (μs)")
    print(str(RUN_TIME / 1000000000) + " seconds")  # to return seconds
    # 2 decimals w/ str(round(answer, 2))
    print(str(round(RUN_TIME / 1000000000, 2)) + " seconds (rounded)")
