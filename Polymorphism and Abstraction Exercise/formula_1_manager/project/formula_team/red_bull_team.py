from project.formula_team.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250000
    sponsors = {
        'Oracle': {1: 1500000, 2: 800000},
        'Honda': {8: 20000, 10: 10000}
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


