import unittest
from poke_api_functions import filter_pokemon_by_names
from poke_api_functions import breeding_compatibility
from poke_api_functions import minmax_weight_by_type

class TestSum(unittest.TestCase):
    BASE_POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/?limit="
    POKEMON_SPECIES_API_URL = "https://pokeapi.co/api/v2/pokemon-species/"
    POKEMON_TYPES_API_URL = "https://pokeapi.co/api/v2/type/"
    POKEMON_NAME = "charmander"
    POKEMON_TYPE = "fighting"

    def test_filter_pokemon_by_names(self):
        number_pokemon = filter_pokemon_by_names(self.BASE_POKEMON_API_URL,\
                                                 self.POKEMON_SPECIES_API_URL)
        self.assertEqual(type(number_pokemon), int, "Not returning the right type of value")

    def test_breeding_compatibility(self):
        number_matches = breeding_compatibility(self.POKEMON_SPECIES_API_URL, self.POKEMON_NAME)
        self.assertEqual(type(number_matches), int, "Not returning the right type of value")

    def test_minmax_weight_by_type(self):
        minmax_weight = minmax_weight_by_type(self.POKEMON_TYPES_API_URL, self.POKEMON_TYPE)
        self.assertEqual(type(minmax_weight), list, "Not returning the right type of value")

if __name__ == '__main__':
    unittest.main()
