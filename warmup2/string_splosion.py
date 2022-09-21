# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    retval = ""
    for x in range(len(str) + 1):
        retval = retval + str[:x]
    return retval

print(string_splosion("Code"))