# Function to calculate readability score of text
def calculate_readability_score(text):

    # Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)

    # Initialise the word counters
    word_count = len(words) # Number of words in list
    short_word_count = 0
    
    complexWords = 0
    for word in words:
        syllables = 0
        for i in range(len(word)):
            if word[i] in "aeiou":
                syllables += 1
                if (word[i] == "e") and (i == len(word) -1):
                    syllables -= 1
        if syllables >= 3:
            complexWords += 1
        
        
        if len(word) <= 2: 
            short_word_count += 1

    # Initialise the number of sentences
    sentence_count = text.count(".")
    sentence_count += text.count("!")
    # Calculate the readability score
    
    
    score = 0.4*((word_count/sentence_count)+100*((word_count-short_word_count)/word_count))
    
    
    score = round(score, 2) # Round the score to 2 d.p.

    return score, short_word_count, complexWords

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1
score1, shorties1, complexWords1 = calculate_readability_score(text1)
print("Short words:",shorties1)
print("Complex words:",complexWords1)
print("Readability Score:", score1, "\n")
score2, shorties2, complexWords2 = calculate_readability_score(text2)
print("Short words:",shorties2)
print("Complex words:",complexWords2)

print("Readability Score:", score2, "\n")



if score1 == score2:
    print("Both scores are the same")
elif score1 < score2:
    print("The first text is easier to read")
elif score2 < score1:
    print("The second text is easier to read")