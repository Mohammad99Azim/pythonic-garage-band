from abc import abstractmethod


class Musician:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def __str__(self):
        return str(f"My name is {self.name} and I play {self.machine}")

    def __repr__(self):
        return f'{self.job} instance. Name = {self.name}'

    def get_instrument(self):
        return self.machine

    def play_solo(self):
        return self.playing


class Band(Musician):
    # instances = []
    #
    # def __init__(self, name, members):
    #     self.name = name
    #     self.members = members
    #     self.instances.append(self)

    # def __str__(self):
    #     return str(f"My name is {self.name} and I play {self.machine}")
    #
    # def __repr__(self):
    #     return f'{self.job} instance. Name = {self.name}'

    # def play_solo(self):
    #     return self.playing

    def play_solos(self):
        play_list = []
        for solo in self.members:
            play_list.append(solo.play_solo())
        return play_list

    @classmethod
    def to_list(cls):
        return cls.instances

    # def get_instrument(self):
    #     return self.machine


class Guitarist(Band):
    def __init__(self, name):
        self.name = name
        self.machine = "guitar"
        self.job = "Guitarist"
        self.playing = "face melting guitar solo"


class Drummer(Band):
    def __init__(self, name):
        self.name = name
        self.machine = "drums"
        self.job = "Drummer"
        self.playing = "rattle boom crash"


class Bassist(Band):
    def __init__(self, name):
        self.name = name
        self.machine = "bass"
        self.job = "Bassist"
        self.playing = "bom bom buh bom"