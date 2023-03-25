# Part 1 - Using a Data Source
# Newspaper Articles

from newspaper import Article
from nltk.corpus import stopwords
from collections import Counter
import nltk
nltk.download('punkt')


# get the URL
url = 'https://www.nytimes.com/2023/03/21/technology/google-bard-chatbot.html'

# download the article
article = Article(url)
article.download()

# parse the article (downloads article's HTML content, extracts main text, performs natural language processing tasks to extract useful info from text)
article.parse()
article_text = article.text
# Output: For more than three months, Google executives have watched as projects at Microsoft and. . .
print(article_text)

##  SUMMARY STATISTICS  ##

# 1. INSTALL NLTK (Natural Language Toolkit) in terminal
# then import nltk
#   processses human language data for part-of-speech tagging, sentimenbt analysis, full sentence parsing

# import Counter
"""
COUNTER:
    - counts and summarizes word frequencies in text
    - comes from the "collections" module, which is a built-in Python module that allows you to used 
      specialized container types for lists, dictionaries, sets, and tuples
"""

# download stopwords from nltk
nltk.download('stopwords')

## repeat steps from earlier example ##
# get URL
url = 'https://www.nytimes.com/2023/03/21/technology/google-bard-chatbot.html'

# download the article
article = Article(url)
article.download()

# parse the article
article.parse()

# get the text
text = article.text

## Removing Stop Words ##
"""
STOP WORDS: 
    - words that occur frequently in text but don't provide any useful info for analysis.
    - e.x. the, and, a

reduces the size of text data and improves accuracy of analysis
"""
# after downloading stopwords from nltk as shown above, import stopwords from the subpackage 'nltk.corpus'.


def remove_stop_words(text):
    """
    This function:
        1. tokenizes the text
        2. gets the stop words from the tokens
        3. removes stop words from the tokens
    """

    # tokenize the text
    """
    tokenize - break text into smaller units called tokens (words, phrases, or characters) 
            preprocessing step in natural language processing (NLP) to make text easier to work with

    TOKENIZATION USES:
        1. Counting word frequencies 
        2. Text normalization (converting all words to lowercase, removing punctuation, etc.)
        3. Machine learning models

        ** Note: this information is generated from asking ChatGPT.
    """
    # alternative would be tokens = word_tokenize(text) if you import the method at the beginning of the script instead.
    tokens = nltk.word_tokenize(text)

    # .words() method retrieves a list of stopwords for a specific language, in this case English.
    # convert to a set bc sets get the job done in a less computationally expensive way.
    stop_words = set(stopwords.words('english'))

    # remove stop words from the tokens using list comprehension
    """
    LIST COMPREHENSION:
        - concise, efficient alternative to for loop
        - list comprehension creeates a new list that contains all the words from the tokens list that are not in the stop_words set
        - .lower() method is used to convert all words to lowercase so case sensitivity is not an issue when checking for stop words
    
      Alternative: for loop for removing stop words 
        filtered_tokens = []  
        for word in tokens:
            if word.lower() not in stop_words:
                filtered_tokens.append(word)

    Breaking down List Comprehension wording:
        [word for word in tokens if word.lower() not in stop_words]
    - 'for' keyword loops over iterable objects and generates a new list containing only words that satisfy the condition of not being in the stop words list
    - the first 'word' before 'for' creates a new list called 'filtered_tokens', which will contain only the words from 'text' that pass the condition 'word.lower() not in stop_words'
    - name each of these words that satisfy the condition as 'word' as directed by the second 'word' in the list comprehension
        - the second 'word' after 'for' is a placeholder variable that takes on each value in the 'tokens' list as the loop iterates through it
    
    - both 'word's refer to the same thing, but don't have to be called the same name bc they just happen to refer to the same element in the list as separate expressions (Idk if 'expressions' is the right terminology)
    - they can be called any variable name bc they are placeholders
    """
    filtered_tokens = [
        word for word in tokens if word.lower() not in stop_words]

    return filtered_tokens


def get_top_words(text, num_words=10):
    # assign the called function to a variable name so that the variable can be called for future use without having to type out the function
    # like in the 'word_freq' variable below
    clean_token = remove_stop_words(text)

    # get the word frequencies
    word_freq = Counter(clean_token)

    # get the 10 most common words
    # .most_common() is a built-in function in 'collections' module; the returned list is sorted from most frequent to least frequent
    top_words = word_freq.most_common(10)

    # print the top 10 words
    for word, freq in top_words:
        print(f"{word}: {freq}")


print(get_top_words(text))
