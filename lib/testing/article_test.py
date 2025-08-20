import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        # comment out the next two lines if using Exceptions
        # article_1.title = 500
        # assert article_1.title == "How to wear a tutu with style"
        
        assert isinstance(article_1.title, str)

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article(author, magazine, 500)

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= len(article_1.title) <= 50

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article(author, magazine, "Test")

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")

    def test_has_an_author(self):
        """article has an author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert article_1.author == author_1
        assert article_2.author == author_2

    def test_author_of_type_author_and_mutable(self):
        """author is of type Author and mutable"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert isinstance(article_1.author, Author)
        assert isinstance(article_2.author, Author)
        
        article_1.author = author_2
        assert isinstance(article_1.author, Author)
        assert article_1.author.name == "Nathaniel Hawthorne"

    def test_has_a_magazine(self):
        """article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine_and_mutable(self):
        """magazine is of type Magazine and mutable"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert isinstance(article_1.magazine, Magazine)
        assert isinstance(article_2.magazine, Magazine)
        
        article_1.magazine = magazine_2
        assert isinstance(article_1.magazine, Magazine)
        assert article_1.magazine.name == "AD"

    def test_get_all_articles(self):
        """Article class has all attribute"""
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all) == 2
        assert article_1 in Article.all
        assert article_2 in Article.all
