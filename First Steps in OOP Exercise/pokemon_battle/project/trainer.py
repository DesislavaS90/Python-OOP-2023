from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = '\n'.join(f'- {p.pokemon_details()}' for p in self.pokemons)
        return f'Pokemon Trainer {self.name}\n' \
               f'Pokemon count {len(self.pokemons)}\n' \
               f'{result}'


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())