# Houm - Coding challenge

## Solution Overview

As requested, the solution has three different functions, each of which return an answer for the three
questions required in the challenge. A detailed description of each function is given as docstrings
in the relevant poke_api_functions.py file. Also, a file for unit tests was added, it basically checks 
if the type of data that each function returns is the one we are expecting.

API requests to the pokeAPI are made directly from Python code by using the "requests" library. Each function
and the code in general was written in a way that we can make as less requests as possible to the pokeAPI. Besides,
it was also written in a way that we can perform a low amount of loops and iterations. 

Finally, pylint was used to improve the quality of the code.

-----------------------------------------
## Approach and Methodology

First we define the base URLs for our purposes as constants.

In the order each method is called:

**filter_pokemon_by_names** This function is designed to answer question 1. It receives two urls as arguments, the first 
one to retrieve pokemon's names, and the second one to retrieve the number of pokemon existent as base species (898). The function
returns a number, which is the number of pokemon with "at" AND two "a" in their names.

**breeding_compatibility** This function is designed to answer question 2. It receives two arguments. The first an URL to get pokemon's base form data from pokeAPI and the second is the pokemon name to search for breeding matches, this can vary as needed (current is raichu, as per the challenge). Given the mentioned data, we look for the egg group of the requested pokemon, and then we get the URLs for those egg groups to search for the pokemon names each egg group has. In order to avoid duplicates, I used set(), and return a number which is the lenght of the set. 

**minmax_weight_by_type** This function is designed to answer question 3. It receives two arguments. The first an URL to get data for a type of pokemon, the second is the specific pokemon type from which we want its max and min weight (current is fighting, as per the challenge). Given the mentioned data, we get the information for the pokemon type specified, and from there we get the URLs to retrieve data for each pokemon of the given type. Finally, we iterate over the data of each pokemon to get its weight. The function return a list that contains the max and min weight for the given pokemon type.

-----------------------------------------
## Instructions to run

The module was constructed using Python 3.8, and you need to run: pip install -r requirements.txt to
install any missing dependencies.

"poke_api_function.py" can be run from any console.

Using console on Linux, by running: python poke_api_function.py
Gives the following output:

Pokemon number containing "at" and two "a" in their names: 9 \
The number of pokemon raichu can breed with is: 294 \
Maximum and minimun weight of G1 fighting type pokemon: [1300, 195] \

Finally, you can run the unit tests by using python test_poke_api_function.py and check that 
they are working correctly.
