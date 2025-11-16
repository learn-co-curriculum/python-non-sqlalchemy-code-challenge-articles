# many_to_many.py

class Article:
    all = []  # Class-level list to track all Article instances

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be 5-50 characters long")
        self._title = title  # Immutable
        self.author = author  # Mutable
        self.magazine = magazine  # Mutable
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name cannot be empty")
        self._name = name  # Immutable

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all articles by this author"""
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        """Return unique magazines this author has written for"""
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        """Create a new article for this author"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique categories of magazines the author has written for"""
        return list({m.category for m in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise TypeError("Name and category must be strings")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be 2-16 characters")
        if len(category) == 0:
            raise ValueError("Category must be at least 1 character")
        self.name = name  # Mutable
        self.category = category  # Mutable

    def articles(self):
        """Return all articles written for this magazine"""
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        """Return unique authors who wrote for this magazine"""
        return list({a.author for a in self.articles()})

    def article_titles(self):
        """Return titles of all articles in this magazine"""
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        """Return authors with more than 2 articles in this magazine"""
        return [
            author for author in self.contributors()
            if len([a for a in self.articles() if a.author is author]) > 2
        ]
