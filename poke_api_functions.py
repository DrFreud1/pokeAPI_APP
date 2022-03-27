
"""
The following module contains three functions each of
which answers the questions in the challenge, the functions
in this module are written in the order they are requested
in the challenge document.

Written by: Santiago Pozo Ruiz

"""

from urllib.parse import urlparse
import requests

def filter_pokemon_by_names(base_api_url: str, pokemon_species_url: str) -> int:
    """Function to get the pokemon filtered by names
    as specified in the challenge.

    The number of species of pokemon's base form is
    taken into account for this task.

    Args:
        base_api_url (str): URL to get pokemon data from pokeAPI.
        pokemon_species_url (str): URL to get pokemon's base
        form data from pokeAPI.

    Returns:
        int: Number of pokemon existen from name specification.

    """
    pokemon_set = set()
    pokemon_count = requests.get(url=pokemon_species_url).json()['count']
    pokemon_species_data = requests.get(url=base_api_url + str(pokemon_count)).json()
    pokemon_names = [pokemon['name'] for pokemon in pokemon_species_data['results']]
    for pokemon in pokemon_names:
        if ("at" in pokemon) and (pokemon.count('a') == 2):
            pokemon_set.add(pokemon)
    return len(pokemon_set)


def breeding_compatibility(pokemon_species_url: str, pokemon_name: str) -> int:
    """Function to get the number of breeding matches
    for a specified pokemon.

    Args:
        pokemon_species_url (str): URL to get pokemon's base
        form data from pokeAPI.
        pokemon_name (str): Pokemon name to search for breeding matches

    Returns:
        int: Number of breeding matches for specified pokemon.

    """
    matches = set()
    pokemon_egg_group_data = requests.get(url=pokemon_species_url + pokemon_name)\
        .json()['egg_groups']
    egg_groups_urls = [egg_group['url'] for egg_group in pokemon_egg_group_data]
    for url in egg_groups_urls:
        egg_group_data = requests.get(url=url).json()
        matches |= {poke['name'] for poke in egg_group_data['pokemon_species']}
    return len(matches)


def minmax_weight_by_type(pokemon_type_url: str, type_name: str) -> list():
    """Function to get the maximum and minimum weight for
    a specified pokemon type of the first generation (Kanto).

    Args:
        pokemon_type_url (str): URL to get pokemon types information.
        type_name (str): Type of pokemon to search for max and min weight.

    Returns:
        list: List with two elements which are the maximum and minimun weight
        of the specified type of pokemon.

    """
    weights_list = list()
    max_min_weight = list()
    pokemon_type_info = requests.get(url=pokemon_type_url + type_name).json()
    pokemon_info = [pokemon['pokemon'] for pokemon in pokemon_type_info['pokemon']]
    for pokemon in pokemon_info:
        parsed_pokemon_url = urlparse(pokemon['url'])
        if int(parsed_pokemon_url.path.rsplit("/", 2)[-2]) <= 151:
            pokemon_data = requests.get(url=pokemon['url']).json()
            weights_list.append(pokemon_data['weight'])
    max_min_weight.append(max(weights_list))
    max_min_weight.append(min(weights_list))
    return max_min_weight


if __name__ == "__main__":
    BASE_POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/?limit="
    POKEMON_SPECIES_API_URL = "https://pokeapi.co/api/v2/pokemon-species/"
    POKEMON_TYPES_API_URL = "https://pokeapi.co/api/v2/type/"

    ANSWER_QUESTION_1 = filter_pokemon_by_names(BASE_POKEMON_API_URL, POKEMON_SPECIES_API_URL)
    ANSWER_QUESTION_2 = breeding_compatibility(POKEMON_SPECIES_API_URL, 'raichu')
    ANSWER_QUESTION_3 = minmax_weight_by_type(POKEMON_TYPES_API_URL, 'fighting')

    print(f"Pokemon number containing \"at\" and two \"a\" in their names: {ANSWER_QUESTION_1} \n"
          f"The number of pokemon raichu can breed with is: {ANSWER_QUESTION_2} \n"
          f"Maximum and minimun weight of G1 fighting type pokemon: {ANSWER_QUESTION_3}")
