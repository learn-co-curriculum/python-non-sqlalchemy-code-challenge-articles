class Article:
    all = []
    def __init__(self, author, magazine, title):
        if isinstance(title, str):
            if len(title) >= 5:
                if len(title) <= 50:
                    self._title = title
                else:
                    self._title = None
            else:
                self._title = None
        else:
            self._title = None
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass


class Author:
    def __init__(self, name):
        if isinstance(name, str):
            if len(name) > 0:
                self._name = name
            else:
                self._name = None
        else:
            self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        result = []
        for x in Article.all:
            if x.author == self:
                result.append(x)
        return result

    def magazines(self):
        m = []
        for a in self.articles():
            if a.magazine:
                if a.magazine not in m:
                    m.append(a.magazine)
        if len(m) > 0:
            return m
        else:
            return None

    def add_article(self, magazine, title):
        art = Article(self, magazine, title)
        return art

    def topic_areas(self):
        t = []
        for a in self.articles():
            if a.magazine:
                cat = a.magazine.category
                if cat not in t:
                    t.append(cat)
        if len(t) > 0:
            return t
        return None


class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str):
            if len(name) >= 2:
                if len(name) <= 16:
                    self._name = name
                else:
                    self._name = None
            else:
                self._name = None
        else:
            self._name = None
        if isinstance(category, str):
            if len(category) > 0:
                self._category = category
            else:
                self._category = None
        else:
            self._category = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if len(value) >= 2 and len(value) <= 16:
                self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str):
            if len(value) > 0:
                self._category = value

    def articles(self):
        res = []
        for x in Article.all:
            if x.magazine == self:
                res.append(x)
        return res

    def contributors(self):
        auth = []
        for a in self.articles():
            if a.author:
                if a.author not in auth:
                    auth.append(a.author)
        if len(auth) > 0:
            return auth
        return None

    def article_titles(self):
        tit = []
        for a in self.articles():
            tit.append(a.title)
        if len(tit) > 0:
            return tit
        return None

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            if a.author:
                if a.author in counts:
                    counts[a.author] = counts[a.author] + 1
                else:
                    counts[a.author] = 1
        res = []
        for author in counts:
            if counts[author] > 2:
                res.append(author)
        if len(res) > 0:
            return res
        return None