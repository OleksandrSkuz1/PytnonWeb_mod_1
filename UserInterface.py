from info import Record, Field, Name, Phone, Birthday, Email, Status, Note

from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands_info(self):
        pass


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(contact)

    def display_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(note)

    def display_commands_info(self):
        print("Available commands:")
        print("- view contacts")
        print("- view notes")
        print("- view commands info")



