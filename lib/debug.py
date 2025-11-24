# lib/debug.py
from author import Author
from magazine import Magazine
from article import Article

author = Author("Carrie Bradshaw")
mag1 = Magazine("Vogue", "Fashion")
mag2 = Magazine("GQ", "Lifestyle")

article1 = author.add_article(mag1, "How to wear a tutu")
article2 = author.add_article(mag1, "Becoming a fashion icon")
article3 = author.add_article(mag2, "NYC Nights")
article4 = Article(author, mag1, "Top 10 Handbags of 2025")

print(Magazine.top_publisher().name)  # Should print "Vogue"