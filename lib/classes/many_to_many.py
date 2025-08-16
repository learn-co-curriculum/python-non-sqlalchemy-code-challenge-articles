class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string")
        self.name = name.strip()

    def __repr__(self):
        return f"Author({self.name})"


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
                    raise Exception("Category must be a string")
        if len(value.strip()) == 0:
            raise Exception("Category cannot be empty")
        self._category = value

    def __repr__(self):
        return f"Magazine({self.name}, {self.category})"


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title  # immutable (no setter)

    def __repr__(self):
        return f"Article({self.title}, {self.author}, {self.magazine})"

    @classmethod
    def articles(cls):
        return cls.all

    @classmethod
    def contributors(cls):
        return list(set(article.author for article in cls.all))

    @classmethod
    def article_titles(cls):
        return [article.title for article in cls.all]

    @classmethod
    def contributing_authors(cls):
        authors = {}
        for article in cls.all:
            authors[article.author] = authors.get(article.author, 0) + 1
        return [author for author, count in authors.items() if count > 2]