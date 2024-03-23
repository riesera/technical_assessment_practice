"""This is a practice question for a technical interview. The goal is as follows:
Given a list, find the mode. If there is more than 1 mode, return the mode that appears in the list first.
If there is no mode, return -1"""
def findMode(array):

    #If the list is empty, there is no mode so return -1
    if not array:
        return -1

    mode_dict = {}

    #Count number of times each number appears and save in a data structure
    for number in array:

        #If the number is already in the dictionary, add 1 to its count
        if str(number) in mode_dict:
            count = mode_dict[str(number)]
            count += 1
            mode_dict[str(number)] = count

        #If it's not already in the dictionary, add it with count of 1
        else:
            mode_dict[str(number)] = 1

    dict_length = len(list(mode_dict.keys()))

    #If all the numbers appear the same amount of times, return -1
    #Initialize count to the first value in the dictionary for comparing
    count = list(mode_dict.values())[0]
    no_mode = True

    #Check if all the counts are the same
    for c in mode_dict.values():
        if count == c:
            continue
        else:
            no_mode = False

    #If all the counts are the same, return -1 because there is no mode
    if no_mode == True:
        return -1

    #Find the number that appears the most times and return it
    search = max(mode_dict.values())
    mode = []

    while not mode:
        mode = list(mode_dict.keys())[list(mode_dict.values()).index(search)]

    return mode



if __name__ == '__main__':

    #Test cases
    print(findMode([]))
    print(findMode([0, 0, 0, 0]))
    print(findMode([1, 1, 1, 2]))
    print(findMode([1, 2, 2, 3]))
    print(findMode([10, 10, 2, 2, 3]))
