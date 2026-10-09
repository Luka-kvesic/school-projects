# Question 16(a)
# Examination Number:Luka kvesic

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word1Comparison = word1.upper()
word2Comparison = word2.upper()
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1Comparison) == sorted(word2Comparison)):
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is NOT an anagram of", word2)
    
if is_anagram(word1Comparison, word2Comparison):
    print(word1, "is an anagram of", word2)
elif not is_anagram(word1Comparison, word2Comparison):
    print(word1, "is NOT an anagram of", word2)


phrase = input("Enter a phrase: ")
phraseComparison = phrase.replace(" ","")
phraseComparison = phraseComparison.upper()
if (sorted(word1Comparison) == sorted(phraseComparison)):
    print(word1, "is an anagram of", phrase)
else:
    print(word1, "is NOT an anagram of", phrase)
if (sorted(word2Comparison) == sorted(phraseComparison)):
    print(word2, "is an anagram of", phrase)
else:
    print(word2, "is NOT an anagram of", phrase) 
    
