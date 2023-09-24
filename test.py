from project.space_station import SpaceStation

space_station = SpaceStation()
space_station.add_astronaut("Biologist", "Rosalin")
space_station.add_astronaut("Meteorologist", "Gosho")
# space_station.add_astronaut("Geodesist", "Pesho")
# space_station.add_astronaut("Biologist", "ivan")
# space_station.add_astronaut("Meteorologist", "Ana")
# space_station.add_astronaut("Biologist", "Rex")
# space_station.add_astronaut("Geodesist", "Tom")

space_station.add_planet("Mars", "Item1, Item2, Item3, Item4, Item5")
space_station.send_on_mission("Mars")

# for astronaut in space_station.astronaut_repository.astronauts:
#     astronaut.oxygen = 29

print(space_station.astronaut_repository.astronauts[0].increase_oxygen(2))
print(space_station.report())



