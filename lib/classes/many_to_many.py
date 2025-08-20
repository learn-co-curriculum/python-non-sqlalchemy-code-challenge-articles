class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name.strip()

    @property
    def name(self):
        return self._name   # immutable, no setter

    def articles(self):
        """Return a list of Article objects written by this author"""
        from classes.many_to_many import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return a unique list of Magazine objects this author has contributed to"""
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        """Create a new Article for this author in the given magazine"""
        from classes.many_to_many import Article, Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique list of categories this author has contributed to, or None if no articles"""
        if not self.articles():
            return None
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories)

    def __repr__(self):
        return f"Author({self.name})"

     
class Magazine:
    all = []  # keep track of all Magazine instances

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)  # store each instance

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

    @classmethod
    def top_publisher(cls):
        """
        Return the Magazine instance with the most articles.
        Return None if there are no articles at all.
        """
        from classes.many_to_many import Article

        if not Article.all:   # no articles created yet
            return None

        # find the magazine with the largest number of articles
        return max(cls.all, key=lambda mag: len(mag.articles()))

    # ---------------------------
    # Relationship methods
    # ---------------------------

    def articles(self):
        """Return all Article objects published in this magazine"""
        from classes.many_to_many import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique Author objects that have written for this magazine"""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Return a list of titles of all articles for this magazine, or None if none"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """
        Return a list of Authors who have written more than 2 articles for this magazine.
        Return None if no such authors exist.
        """
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    def __repr__(self):
        return f"Magazine({self.name}, {self.category})"


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author          # now goes through setter
        self.magazine = magazine      # now goes through setter
        self.title = title            # use setter for validation
        Article.all.append(self)

    # ---------- AUTHOR ----------
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from classes.many_to_many import Author  # avoid circular import at top
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # ---------- MAGAZINE ----------
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from classes.many_to_many import Magazine
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value

    # ---------- TITLE ----------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if not (5 <= len(value) <= 50):
            raise Exception("Title must be between 5 and 50 characters")
        self._title = value

    def __repr__(self):
        return f"Article(title='{self.title}', author={self.author}, magazine={self.magazine})"
