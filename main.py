destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Travelling to faraway lands
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
# print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris, France"))


def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

attractions = [[] for location in destinations]
print(attractions)

