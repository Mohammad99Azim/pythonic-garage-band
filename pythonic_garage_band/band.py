from abc import abstractmethod


class Musician:
    members = []


class Band(Musician):

    def __init__(self, name, members):
        self.name = name
        self.members = members

    @abstractmethod
    def play_solo(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    def __str__(self):
        return str(f"My name is {self.name} and I play {self.instrument}")

    def __repr__(self):
        return f"{self.job} instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        pass


class Guitarist(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"
        self.job = "Guitarist"

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"
        self.job = "Bassist"

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Band):
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"
        self.job = "Drummer"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return "rattle boom crash"


if __name__ == "__main__":
    nirvana = Band("Nirvana", [])
    print(nirvana.name)

# def __init__(self, name):
#     self.name = name
#
# def __str__(self):
#     return str(f"My name is {self.name} and I play guitar")
#
# def __repr__(self):
#     return f"Guitarist instance. Name = {self.name}:
