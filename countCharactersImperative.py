import time
import math


def count_total_characters(a_character_list):
    return len(a_character_list)


def build_character_list(a_file):
    the_list = []
    for every_line in a_file:  # breaks it up by line
        for every_character in every_line:  # counts newline '\n' character as well. minus those is 229
            the_list.append(every_character.capitalize())  # don't want to recount upper/lower case

    return the_list


def build_unique_character_list(character_list):
    uniques_found = []
    for some_character in character_list:
        if some_character in uniques_found:
            continue
        else:
            uniques_found.append(some_character)

    return uniques_found


def count_uniques(a_character_list, uniques_list):  # can use microsoft word find function to check accuracy
    count = 0
    linked_dictionary = {}
    for someUnique in uniques_list:
        for aCharacter in a_character_list:
            if aCharacter == someUnique:
                count += 1
        # go through entire character list
        # print("Total found for " + str(someUnique) + ": " + str(count))
        linked_dictionary[someUnique] = count
        count = 0

    return linked_dictionary


def find_probabilities(a_unique_dictionary, total_characters):
    the_probabilities = {}
    for each_key in a_unique_dictionary:
        amount_of_each_key_found = a_unique_dictionary[each_key]
        probability_of_each_key = amount_of_each_key_found / total_characters
        probability_of_each_key = round(probability_of_each_key, 4)
        the_probabilities[each_key] = probability_of_each_key
    return the_probabilities


if __name__ == "__main__":
    startClock = time.perf_counter_ns()
    myTextFile = open("C:/Users/Mikaela/Documents/Spring2020/CS441 Progrm LangDes&Imp/Final Project/testFile.txt", "r")

    characterList = build_character_list(myTextFile)
    # print("Total lines found: " + str(lineCount))  # total: 4
    # print("Total characters found: " + str(characterCount))  # total: 233
    # print(len(characterList))  # returns 233
    TotalCharacters = count_total_characters(characterList)
    print(TotalCharacters)

    uniqueCharacters = build_unique_character_list(characterList)
    print(len(uniqueCharacters))  # returns 36
    # print("Total unique characters found: " + str(len(uniqueCharacters)))  # total: 36 (39 if not capitalized)
    myDictionary = count_uniques(characterList, uniqueCharacters)
    print(myDictionary)  # show whole dictionary
    myProbabilities = find_probabilities(myDictionary, TotalCharacters)
    print(myProbabilities)

    sumOfTheInformation = 0
    for eachUniqueCharacterFound in myDictionary:
        numberOfTimesItOccurs = myDictionary[eachUniqueCharacterFound]
        if eachUniqueCharacterFound in myProbabilities:
            probabilityOfTheCharacter = myProbabilities[eachUniqueCharacterFound]
        informationForThisCharacter = round((numberOfTimesItOccurs * (-probabilityOfTheCharacter) *
                                             math.log(probabilityOfTheCharacter, 2)), 6)
        sumOfTheInformation += informationForThisCharacter

    sumOfTheInformation = round(sumOfTheInformation, 6)  # this value will reduce with groups of characters
    print("TOTAL SUM OF INFORMATION: " + str(sumOfTheInformation))

    runTime = ((time.perf_counter_ns()) - startClock)  # end time - start time to get duration
    print(str(runTime) + " nanoseconds")
    print(str(runTime / 1000) + " microseconds (μs)")
    print(str(runTime / 1000000000) + " seconds")  # to return seconds
    # 2 decimals w/ str(round(answer, 2))
    print(str(round(runTime / 1000000000, 2)) + " seconds (rounded)")
