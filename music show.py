from abc import ABC, abstractmethod

# Abstract Parent Class
class Instrument(ABC):

    def __init__(self, name):
        self.name = name
        print(f"{self.name} instrument is ready!")

    @abstractmethod
    def sound(self):
        pass


# Child Class 1
class Piano(Instrument):

    def __init__(self):
        super().__init__("Piano")

    def sound(self):
        print("Piano Sound: Plink Plonk 🎹")


# Child Class 2
class Guitar(Instrument):

    def __init__(self):
        super().__init__("Guitar")

    def sound(self):
        print("Guitar Sound: Strum Strum 🎸")


# Child Class 3
class Drum(Instrument):

    def __init__(self):
        super().__init__("Drum")

    def sound(self):
        print("Drum Sound: Boom Boom 🥁")


# Main Program
print("=== Musical Instrument Sound Show ===\n")

p = Piano()
g = Guitar()
d = Drum()

print("\nPlaying Instruments...\n")

p.sound()
g.sound()
d.sound()