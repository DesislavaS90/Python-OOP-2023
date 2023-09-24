from project.player import Player
from project.supply.supply import Supply


class Controller:
    SUPPLY_TYPE = ["Food", "Drink"]

    def __init__(self):
        self.supplies = []
        self.players = []

    def add_player(self, *player1: Player):
        result = []
        for p in player1:
            if p not in self.players:
                self.players.append(p)
                result.append(p.name)
        return f'Successfully added: {", ".join(n for n in result)}'

    def add_supply(self, *supply1: Supply):
        for s in supply1:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        player = [p for p in self.players if p.name == player_name]
        supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]

        if not player:
            return
        if sustenance_type not in self.SUPPLY_TYPE:
            return

        player = player[0]

        if player.stamina == 100:
            return f'{player_name} have enough stamina.'

        if not supply:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')

        last_supply = supply[-1]

        if player.stamina + last_supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += last_supply.energy

        for i in range(len(self.supplies)-1, -1, -1):
            if last_supply == self.supplies[i]:
                self.supplies.pop(i)
                return f'{player_name} sustained successfully with {last_supply.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        result = []
        p1 = [p for p in self.players if p.name == first_player_name][0]
        p2 = [p for p in self.players if p.name == second_player_name][0]

        if p1.stamina == 0:
            result.append(f'Player {first_player_name} does not have enough stamina.')
        if p2.stamina == 0:
            result.append(f'Player {second_player_name} does not have enough stamina.')
        if result:
            return "\n".join(result)

        if p1.stamina < p2.stamina:
            result = p1.stamina / 2
            if p2.stamina - result <= 0:
                p2.stamina = 0
                return f'Winner: {first_player_name}'
            p2.stamina -= result

            result = p2.stamina / 2
            if p1.stamina - result <= 0:
                p1.stamina = 0
                return f'Winner: {second_player_name}'
            p1.stamina -= result

        else:
            result = p2.stamina / 2
            if p1.stamina - result <= 0:
                p1.stamina = 0
                return f'Winner: {second_player_name}'
            p1.stamina -= result

            result = p1.stamina / 2
            if p2.stamina - result <= 0:
                p2.stamina = 0
                return f'Winner: {first_player_name}'
            p2.stamina -= result

        if p1.stamina > p2.stamina:
            return f'Winner: {first_player_name}'
        else:
            return f'Winner: {second_player_name}'

    def next_day(self):

        for p in self.players:
            if p.stamina - p.age * 2 <= 0:
                p.stamina = 0
            else:
                p.stamina -= p.age * 2
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):

        result = []

        for p in self.players:
            result.append(p.__str__())

        for s in self.supplies:
            result.append(s.details())

        return "\n".join(result)
