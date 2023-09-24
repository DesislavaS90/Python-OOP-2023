from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\n"\
                   f"Robots: none"
        return f"{self.name} Secondary Service:\n"\
               f"Robots: {' '.join([r.name for r in self.robots])}"
