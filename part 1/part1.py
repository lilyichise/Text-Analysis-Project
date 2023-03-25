from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)
article.download()
article.parse()
article_text = article.text
# Output: Washington (CNN) -- Not everyone subscribes to a New Year's resolution...
print(article_text)
