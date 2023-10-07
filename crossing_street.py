# %%
from durable.lang import *

with ruleset("crossing_street"):
    # Rule for green light
    @when_all(m.color == "green")
    def green_light(c):
        print("Go.")
    
    # Rule for yellow light
    @when_all(m.color == "yellow")
    def yellow_light(c):
        print("Slow down.")
    
    # Rule for red light
    @when_all(m.color == "red")
    def red_light(c):
        print("Stop.")

# Test the rules with different colors
post("crossing_street", {"color": "red"})
post("crossing_street", {"color": "green"})
post("crossing_street", {"color": "yellow"})
