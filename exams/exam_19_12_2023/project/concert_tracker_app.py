from typing import List

from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        pass

    def create_band(self, name: str):
        pass

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        pass

    def add_musician_to_band(self, musician_name: str, band_name: str):
        pass

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass

