class Field(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"self.{self.name} = {self.value}"

class Code(object):
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = [f"class {self.name}" ]
        if not self.fields:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for field in self.fields:
                lines.append(f"     {field}")
        return "\n".join(lines)

class CodeBuilder:
    def __init__(self, root_name):
        # todo
        self.__code = Code(root_name)

    def add_field(self, type, name):
        # todo
        self.__code.fields.append(Field(type, name))
        return self

    def __str__(self):
        # todo
        return self.__code.__str__()

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)

cb1 = CodeBuilder("")
print(cb1)
