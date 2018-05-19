import json
import lxml
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES

filename = 'data.json'
with open(filename) as dataset:
    pop_data = json.load(dataset)

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code 
    return None

cc_populations = {}

for pop_dict in pop_data:
    country_name = pop_dict['Country Name']
    population = pop_dict['Value']
    code = get_country_code(country_name)
    if code:
        cc_population[code] = population

pop_lvl_1 = {}
pop_lvl_2 = {}
pop_lvl_3 = {}

for code, pop in cc_populations.items():
    if pop < 10000000:
        pop_lvl_1[code] = pop
    elif pop < 1000000000:
        pop_lvl_2[code] = pop
    else:
        pop_lvl_3[code] = pop

worldmap_chart = World()
worldmap_chart.title = '2016 World Population by Country'
worldmap_chart.add('0-10M', pop_lvl_1)
worldmap_chart.add('10M - 1B',pop_lvl_2)
worldmap_chart.add('1Bn+', pop_lvl_3)
worldmap_chart.render_in_browser()


