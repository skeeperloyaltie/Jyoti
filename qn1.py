# Write a logic inside the given fucntion to do the following task on a given input string
# find the number of LIsts, Dictionaries and Tuples that occurs in the input string and return the count in the order of List, 
# Dictionary, Tuples (LDT). That is return 

# "L" + listcount + "D" + dictcount + "T" + tuplecount
# like "L1D0T0"

# 1. Lists are identified with the square bracket []
# 2. Tuples are identified with the paranthesis: ()
# 3. Dictionairies are identified with curly brackets: {}

# if there is no tuple no list and no dictionary are available then return false
# all the opening tokens will have a matching closing token that is All ([{ will have a matching closing token that is ]})
# input and output are case sensitive
# no need to read input from keyboard input will be supplied as a string

                                                                    
def CountListDictTuple(input1):
    listcount = 0
    dictcount = 0
    tuplecount = 0
    # create start and end  tokens for list, dictionary and tuple
    startlist = "["
    endlist = "]"
    startdict = "{"
    enddict = "}"
    starttuple = "("
    endtuple = ")"
    # create a list of start and end tokens
    startend = [startlist, endlist, startdict, enddict, starttuple, endtuple]
    # create the fucntion to check if the input string has a matching start and end token
    def check(input1, startend):
        for i in range(0, len(startend), 2):
            if input1.count(startend[i]) != input1.count(startend[i+1]):
                return False
        return True
    
    # check if the input string has a matching start and end token
    if check(input1, startend) == False:
        return False

    # check if the input string has a list, dictionary or tuple
    if input1.count(startlist) > 0:
        listcount = input1.count(startlist)
    if input1.count(startdict) > 0:
        dictcount = input1.count(startdict)
    if input1.count(starttuple) > 0:
        tuplecount = input1.count(starttuple)
    # create the output string
    output = "L" + str(listcount) + "D" + str(dictcount) + "T" + str(tuplecount)
    
    return output


# test the function
print(CountListDictTuple("[{}]()"))
print(CountListDictTuple("[{}]()[]"))
print(CountListDictTuple("[{}]()[]{}"))
print(CountListDictTuple("[{}]()[]{}()"))
print(CountListDictTuple("[{}]()[]{}()[]"))



    


