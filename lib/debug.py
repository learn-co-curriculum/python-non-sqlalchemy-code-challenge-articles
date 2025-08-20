#!/usr/bin/env python3
# import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")



    # Create some authors
    author1 = Author("Grace")
    author2 = Author("James")

    # Create some magazines
    mag1 = Magazine("Tech Times", "Technology")
    mag2 = Magazine("Health Hub", "Health")

    # Create some articles
    art1 = Article(author1, mag1, "AI in 2025")
    art2 = Article(author1, mag2, "Nutrition Myths")
    art3 = Article(author2, mag1, "Cybersecurity Trends")

    # Test relationships
    print("\n--- Author Tests ---")
    print(f"{author1.name}'s articles:", author1.articles())
    print(f"{author1.name}'s magazines:", author1.magazines())
    print(f"{author1.name}'s topics:", author1.topic_areas())

    print("\n--- Magazine Tests ---")
    print(f"Articles in {mag1.name}:", mag1.articles())
    print(f"Contributors in {mag1.name}:", mag1.contributors())

    print("\n--- Bonus ---")
    print("Top publisher:", Magazine.top_publisher())



    # don't remove this line, it's for debugging!
    # ipdb.set_trace()
