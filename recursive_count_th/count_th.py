'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops
'''
def count_th(word):
     if word.count('th') == 0:
         return 0
     
    
     return word.count('th')


