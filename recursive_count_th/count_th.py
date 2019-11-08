'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # find base case
	# find recursive return that leads to base case
	
    if len(word) < 2: # base case - if word is less than 2 return 0
        return 0
    th = 0 # this int will keep track if there is a th in the string
    if word[-2:] == "th": # check if the last two letters ar `th`
        th += 1

    return th + count_th(word[:len(word)-1]) # recursion happens here. each time the function is called 

wrd = "themostath"
wrd2 = "themothsthath"

print(count_th(wrd))
print(count_th(wrd2))
