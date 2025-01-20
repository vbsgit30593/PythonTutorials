"""
Delegation involves delegating the responsibility of a task to a helper
It doesn't care about how the task is done
Promotes composition over inheritance.
"""


from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, message):
        pass


class ConsolePrinter(Printer):
    def print(self, message):
        print(f"Printing on console: {message = }!")


class FilePrinter(Printer):
    def print(self, message):
        with open("testfile.txt", "w") as f:
            f.write(message)
        
        print("Message written to file!")



# Delegator
class Document:
    def __init__(self, printer: Printer):
        self.printer = printer

    def change_printer(self, printer: Printer):
        self.printer = printer

    def print(self, message):
        self.printer.print(message)


if __name__ == "__main__":
    doc = Document(ConsolePrinter())
    doc.print("Hello!")

    doc.change_printer(FilePrinter())
    doc.print("Hello again!")

    doc.change_printer(ConsolePrinter())
    doc.print("Bye!")