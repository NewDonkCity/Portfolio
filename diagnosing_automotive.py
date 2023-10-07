# %%
from durable.lang import *


with ruleset("diagnosing_automotive"):

    @when_all((m.engine_gets_gas == True) & (m.engine_turns_over == True))
    def problem_is_spark_plugs(c):
        print(c.m)
        print("The problem is spark plugs.")

    # problem_is_battery_or_cables ?
    
    # problem_is_starter_motor ?
    
    # post an event for engine is getting gas?
    
    # what rule is missing to make this comprehensive?
    
    # handle unknown situation?


# %%
from itertools import product

for (
    engine_turns_over,
    lights_come_on,
    gas_in_fuel_tank,
    gas_in_carburator,
) in product([True, False], [True, False], [True, False], [True, False]):
    fact = {
        "engine_turns_over": engine_turns_over,
        "lights_come_on": lights_come_on,
        "gas_in_fuel_tank": gas_in_fuel_tank,
        "gas_in_carburetor": gas_in_carburetor,
    }
    post("diagnosing_automotive", fact)
