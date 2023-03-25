# Text-Analysis-Project
 
Please read the [instructions](instructions.md).  

# 1. Project Overview (~1 paragraph)
I used the data source Newspaper3k to scrape and curate news articles.    
The techniques I used to process or analyze them include using tools in the natural language toolkit as well as the Collections module for more efficient ways of using lists, dictionaries, sets, and tuples.  
I simply hoped to create functioning code and I hope to learn more techniques like the nltk; I also hope to be able to practice the techniques I already know and learn to implement them in more efficient ways in terms of formatting and conciseness.  
  

# 2. Implementation (~1-2 paragraphs + screenshots)
The goal for the code was to take a news article and return the top most frequent words after cleaning up the text file.

Major components in sequential order:  
- Downloading the news article  
- Preparing the article (via stopwords & parse techniques)  
- Counting word frequencies  

After downloading, tokenizing, and parsing the article, run the prepared text through a function that removes stop words (remove_stop_words(text)), finally being incorporated into a function that takes the count of the most common tokens and prints the final result.  
  
One design decision for the code was to use list comprehension versus a standard for loop for writing the conditions for the filtered tokens list. I did this to make the code more concise. Please see the screenshot attached below for reference.  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-25%20at%2012.14.29%20AM.png) 
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-25%20at%2012.14.13%20AM.png)  
  
As for ChatGPT, it helped a lot in not only making my code more concise as with the example above, but in explaining to me why certain techniques are used and why they are written the way they are. Please see the attached screenshots of the many, many, many questions that I asked it.  
  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.06.16%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.06.37%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.07.05%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.07.17%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.07.38%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.30%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.42%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.49%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.56%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.06.03%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.04%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.15%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.05.24%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.03.34%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.04.35%20PM.png)  
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-24%20at%2011.04.57%20PM.png)  


# 3. Results (~2-3 paragraphs + figures/examples)
If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.


# 4 Reflection (~1-2 paragraphs)
From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?

From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?

