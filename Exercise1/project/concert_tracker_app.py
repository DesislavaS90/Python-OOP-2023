from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIAN_TYPE = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        musician_name = [m.name for m in self.musicians]

        if musician_type not in self.VALID_MUSICIAN_TYPE:
            raise ValueError("Invalid musician type!")

        if name in musician_name:
            raise Exception(f"{name} is already a musician!")

        result = self.VALID_MUSICIAN_TYPE[musician_type](name, age)
        self.musicians.append(result)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_name = [b for b in self.bands if b.name == name]

        if band_name:
            raise Exception(f"{name} band is already created!")

        result = Band(name)
        self.bands.append(result)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]

        if concert:
            raise Exception(f"{place} is already registered for {concert[0].genre} concert!")

        result = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(result)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]
        musician = [m for m in self.musicians if m.name == musician_name]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b.name for b in self.bands]
        if band_name not in band:
            raise Exception(f"{band_name} isn't a band!")

        existing_band = [b for b in self.bands if b.name == band_name][0]
        musician = [m for m in existing_band.members if m.name == musician_name]

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        existing_band.members.remove(musician[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        members = set([m.__class__.__name__ for m in band.members])

        if len(members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for member in band.members:
                if member.__class__.__name__ == 'Drummer' and 'play the drums with drumsticks' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == 'Singer' and 'sing high pitch notes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == 'Guitarist' and 'play rock' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for member in band.members:
                if member.__class__.__name__ == 'Drummer' and 'play the drums with drumsticks' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == 'Singer' and 'sing low pitch notes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == 'Guitarist' and 'play metal' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == 'Jazz':
            for member in band.members:
                if member.__class__.__name__ == 'Drummer' and 'play the drums with drum brushes' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == 'Singer' and ('sing high pitch notes' not in member.skills
                                             or 'sing low pitch notes' not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ == 'Guitarist' and 'play jazz' not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

