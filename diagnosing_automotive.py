# %%
from durable.lang import *

# Define the ruleset for diagnosing automotive problems
with ruleset("diagnosing_automotive"):
    # If the engine is getting gas and the engine will turn over, then the problem is the spark plugs.
    @when_all(
        (m.engine_gets_gas == True) & (m.engine_turns_over == True)
    )
    def problem_is_spark_plugs(c):
        print(c.m)
        print("The problem is spark plugs.")

    # If the engine does not turn over and the lights do not come on, then the problem is the battery or cables.
    @when_all(
        (m.engine_turns_over == False) & (m.lights_come_on == False)
    )
    def problem_is_battery_or_cables(c):
        print(c.m)
        print("The problem is battery or cables.")

    # If the engine does not turn over and the lights do come on, then the problem is the starter motor.
    @when_all(
        (m.engine_turns_over == False) & (m.lights_come_on == True)
    )
    def problem_is_starter_motor(c):
        print(c.m)
        print("The problem is starter motor.")

    # If there is gas in the fuel tank and there is gas in the carburetor, then the engine is getting gas.
    @when_all(
        (m.gas_in_fuel_tank == True) & (m.gas_in_carburetor == True) 
    )
    def engine_gets_gas_confirmed(c):
        post(
            "diagnosing_automotive",
            {
                "engine_gets_gas": True,
                "engine_turns_over": c.m.engine_turns_over,
                "lights_come_on": c.m.lights_come_on,
            },
        )

    # If there is no gas in the fuel tank or there is no gas in the carburetor, then it is unknown if the engine is getting gas.
    @when_all(
        (m.gas_in_fuel_tank == False) | (m.gas_in_carburetor == False)
    )
    def engine_gets_gas_unknown(c):
        post(
            "diagnosing_automotive",
            {
                "engine_gets_gas": c.m.engine_gets_gas,
                "engine_turns_over": c.m.engine_turns_over,
                "lights_come_on": c.m.lights_come_on,
            },
        )

    # Handle unknown situation
    @when_all(
        (m.engine_gets_gas == None) | (m.engine_gets_gas == False)
    )
    def problem_is_unknown(c):
        print(c.m)
        print("The problem is unknown.")


# %% Test all possible combinations of facts
from itertools import product

for (
    engine_turns_over,
    lights_come_on,
    gas_in_fuel_tank,
    gas_in_carburetor,
) in product(
    [True, False], [True, False], [True, False], [True, False]
):
    fact = {
        "engine_turns_over": engine_turns_over,
        "lights_come_on": lights_come_on,
        "gas_in_fuel_tank": gas_in_fuel_tank,
        "gas_in_carburetor": gas_in_carburetor,
    }
    post("diagnosing_automotive", fact)
