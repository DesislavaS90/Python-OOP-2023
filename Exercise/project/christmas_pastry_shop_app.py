from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_NAME = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    VALID_BOOTH_TYPE = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        result = [d for d in self.delicacies if d.name == name]
        if result:
            raise Exception(f'{name} already exists!')

        if type_delicacy not in self.VALID_DELICACY_NAME:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        self.delicacies.append(self.VALID_DELICACY_NAME[type_delicacy](name, price))
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        result = [b for b in self.booths if b.booth_number == booth_number]
        if result:
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth not in self.VALID_BOOTH_TYPE:
            raise Exception(f'{type_booth} is not a valid booth!')

        self.booths.append(self.VALID_BOOTH_TYPE[type_booth](booth_number, capacity))
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved]

        if not booth:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth[0].reserve(number_of_people)
        return f'Booth {booth[0].booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth_num = [b for b in self.booths if booth_number == b.booth_number]
        delicacy_n = [d for d in self.delicacies if delicacy_name == d.name]

        if not booth_num:
            raise Exception(f'Could not find booth {booth_number}!')

        if not delicacy_n:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth_num[0].delicacy_orders.append(delicacy_n[0])
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if booth_number == b.booth_number][0]
        bill = booth.price_for_reservation + sum(s.price for s in booth.delicacy_orders)

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        self.income += bill

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'
