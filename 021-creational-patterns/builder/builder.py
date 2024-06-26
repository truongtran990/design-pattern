"""
Imagine you have to create the HTML structure,
You end up with the solution below
"""
text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))


words = ["hello", "world"]
parts = ["<ul>"]
for word in words:
    parts.append(f"    <li>{word}</li>")

parts.append("</ul>")
print("\n".join(parts))

print("*" * 10)

"""
How do you create a complex HTML structure with above way???
Let's do it with builder dp
"""
class HTMLElement(object):
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            indent_content = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{indent_content}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")

        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HTMLBuilder(name)


class HTMLBuilder(object):
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HTMLElement(name=root_name)

    def __str__(self):
        return str(self.__root)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
                HTMLElement(child_name, child_text)
                )

    def add_child_fluent(self, child_name, child_text):
        """
        return itself, create chain method
        """
        self.__root.elements.append(
                HTMLElement(child_name, child_text)
                )
        return self


if __name__ == "__main__":
    builder = HTMLElement.create("ul")
    builder.add_child_fluent("li", "hello")\
        .add_child_fluent("li", "world, ")\
        .add_child_fluent("li", "my")\
        .add_child_fluent("li", "name")\
        .add_child_fluent("li", "is")\
        .add_child_fluent("li", "Truong")\

    print(builder)
