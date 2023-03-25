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
Something interesting I found while doing text analysis was the Collections module.  
I didn't know there were more efficient ways of using dictionaries, lists, tuples, and sets.  
One more efficient technique that I specifically learned from the Collections module is the Counter() technique. It saves space and time bc otherwise, I would've made a for loop with a counter.  
For the future, I am interested in learning more techniques within the Collections module.
![Alt text](../../../../Desktop/Screen%20Shot%202023-03-25%20at%2012.21.54%20AM.png)


# 4 Reflection (~1-2 paragraphs)
From a process point of view, what went well is that I was able to learn a few more new modules and libraries. We are always exposed to new libraries and modules through the classworks and homeworks, but actually exploring it myself and choosing from the broad options made me truly realize how broad and seemingly limitless the possibilities are with Python. It's probably a really obvious realization, but it never really hit me in the same way until this project.  
  
In terms of improvement, I feel that I could've scope the project better using more examples and more text analysis techniques. It just took me so long to figure out one of the techniques that I took a very narrow but deep approach this time, thoroughly going through every line of code and technique. On the other hand, because of this, I feel that I really understand the code that I wrote and have a much better chance of recalling it for future use. It was a time-consuming process, but honestly for me, this was probably a better method to learn code than going through a lot of different text analysis tools and testing them out. I feel that I am better prepared to try out other code and build the base infrastructure because I went through it so thorughly. ChatGPT was a HUGE part of this process in helping me understand (as you saw through the gajillion questions I asked), so I will definitely be using it in the future as I develop my foundations and try to understand why things are built in the way that they are. If anything, I wish I would have known that I should thoroughly go through every line of code and explain it in the sides with the support of ChatGPT. My original idea was to keep the comments minimal to be able to easily see the code that was used, but I realized that it may be better for me to document everything so that I actually remember the individual techniques and don't miss anything that would create difficult gaps for understanding future concepts.   

