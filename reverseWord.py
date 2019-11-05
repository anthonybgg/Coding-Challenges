"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace 
and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

def reverseWord(words : str):
    # Fill this in. 
    worded = words.split()
    ret = ''
    for i in range(len(worded)):
        if i == len(worded):
            ret += worded[i][::-1]
        else:
            ret += worded[i][::-1] + ' '
    return ret
