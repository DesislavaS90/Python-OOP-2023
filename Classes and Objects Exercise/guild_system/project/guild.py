from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        if self.name != player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = 'Unaffiliated'
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        details = '\n'.join([t.player_info() for t in self.players])
        return f'Guild: {self.name}\n' \
               f'{details}'


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
