from project.formula_team.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200000
    sponsors = {
        'Petronas': {1: 1000000, 3: 500000},
        'TeamViewer': {5: 100000, 7: 50000}
    }

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for p in self.sponsors.values():
            for position in p:
                if race_pos <= position:
                    revenue += p[position]
                    break
        revenue -= self.EXPENSES_PER_RACE
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'