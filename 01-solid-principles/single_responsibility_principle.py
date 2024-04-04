"""
A class just have only one responsibility
"""
import os

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count} - {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        """
        The actual things you want to print to standard out when calling print(Journal)
        """
        return "\n".join(self.entries)
    
    # all the above is good, but add some method like save or load data to/from file is violate the srp
    # def save(self, filename):
    #     with open(filename, "w") as f:
    #         f.write(str(self))
    #     print("save successfully!!!")

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(obj, filename):
        with open(filename, "w+") as f:
            f.write(str(obj))
        print("save to file successfully!!!")

    @staticmethod
    def read_from_file(filename):
        with open(filename, "r") as f:
            data = f.read()
            print(f"len of file {filename} is: {len(data)}")
        return data


j = Journal()
j.add_entry("I want to cry")
j.add_entry("I'm tired")
print(f"journal entries: \n{j}")

base_dir = (os.path.dirname(os.path.realpath(__file__)))
filename = f"{base_dir}/journal.txt"
PersistenceManager.save_to_file(j, filename)
PersistenceManager.read_from_file(filename)

