##### MAIN #####
# AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
# CREATE DATE: 31 Mar 2023

# DESC: TextEvaluator is a program that evaluates text for UIs. It
#       returns a readability score, complexity score, and grade level.


### Imports ###
import textstat




### FUNCTIONS ###
# Overall readability score
def overallReadability(text) -> int:
    """
    Generates an aggregated readability score based on scores at https://github.com/textstat/textstat
    text is a string that will be analyzed for readability.
    """
    return textstat.text_standard(text, float_output=False)
      
    

# Calculate reading time
def readingTime(text) -> float:
    """
    Generates an estimated reading time for the entered text.
    text is a string that will be analyzed for this analysis.
    """
    # Note: ms_per_char is the assumed reading time per character in a word.
    return textstat.reading_time(text, ms_per_char=14.69)



# Calculate sentences
def sentenceCount(text) -> int:
    """
    Number of sentences in the entered text
    text is a string analyzed for number of sentences.
    """
    return textstat.sentence_count(text)



# Calculate letters
def letterCount(text) -> int:
    """
    Number of letters in a text
    text is a string analyzed for count
    """
    return textstat.letter_count(text, ignore_spaces=True)

