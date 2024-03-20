class Element:
    def __init__ (self, tag, content = "", attrs = {}):
        self.tag = tag
        self.content = content
        self.attrs = attrs
    
    def render (self):
        attrs = " ".join(
            f'{name}="{value}"'
            for name, value in self.attrs.items()
        )
        attrs = " " + attrs if attrs else attrs
        if isinstance(self.content, Element):
            content = content.render()
        elif isinstance(self.content, list):
            self.content = "".join(
                [
                    item.render() if isinstance(item, Element) else item
                    for item in self.content
                ]
            )
        return f"<{self.tag}{attrs}>{self.content}</{self.tag}>"


class Heading (Element):
    def __init__ (self, content, level = 1, attrs = {}):
        super().__init__(f"h{level}", content, attrs)
        self.level = level


class Link (Element):
    def __init__ (self, content, url, attrs = {}):
        super().__init__(
            "a",
            content,
            attrs | {"href": url}
        )
        self.url = url


class Row (Element):
    def __init__ (self, items, header = False, attrs = {}):
        super().__init__("tr", "", attrs)
        self.header = header
        self.items = items

    def render (self):
        for item in self.items:
            if self.header:
                self.content += Element("th", item).render()
            else:
                self.content += Element("td", item).render()
        
        return super().render()


class Table (Element):
    def __init__ (self, attrs = {"dir": "rtl", "align": "center"}):
        super().__init__("table", "", attrs)
        self.rows = []
    
    def add_row (self, items, header = False):
        self.rows.append(
            items if isinstance(items, Row) else Row(items, header = header)
        )

    def render (self):
        thead = []
        tbody = []

        for row in self.rows:
            if row.header:
                if tbody:
                    self.content += Element("tbody", tbody).render()
                    tbody = []
                thead.append(row)
            else:
                if thead:
                    self.content += Element("thead", thead).render()
                    thead = []
                tbody.append(row)
            
        if thead:
            self.content += Element("thead", thead).render()
        elif tbody:
            self.content += Element("tbody", tbody).render()

        return super().render()