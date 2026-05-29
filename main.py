from owlready2 import *

# LOAD ONTOLOGY FILE
onto = get_ontology("travel.owl").load()

# =========================
# SHOW ALL PLACES
# =========================

print("\n===== PLACES =====\n")

for place in onto.Place.instances():
    print(place.name)

# =========================
# SHOW ALL FOODS
# =========================

print("\n===== FOODS =====\n")

for food in onto.Food.instances():
    print(food.name)

# =========================
# SHOW ALL HOTELS
# =========================

print("\n===== HOTELS =====\n")

for hotel in onto.Hotel.instances():
    print(hotel.name)

# =========================
# SHOW ALL TOURIST PLACES
# =========================

print("\n===== TOURIST PLACES =====\n")

for tourist_place in onto.Tourist_Place.instances():
    print(tourist_place.name)

# =========================
# SHOW FOOD RELATIONSHIPS
# =========================

print("\n===== FOOD RECOMMENDATIONS =====\n")

for food in onto.Food.instances():

    print("Food:", food.name)

    # famousin relationship
    for place in food.famousin:
        print("  Famous in:", place.name)

    print()

# =========================
# SHOW TOURIST PLACE RELATIONSHIPS
# =========================

print("\n===== TOURIST PLACE LOCATIONS =====\n")

for tourist_place in onto.Tourist_Place.instances():

    print("Tourist Place:", tourist_place.name)

    # locatedIn relationship
    for place in tourist_place.locatedIn:
        print("  Located in:", place.name)

    print()

# =========================
# SHOW HOTEL RELATIONSHIPS
# =========================

print("\n===== HOTEL INFORMATION =====\n")

for hotel in onto.Hotel.instances():

    print("Hotel:", hotel.name)

    # nearTo relationship
    for nearby_place in hotel.NearTo:
        print("  Near:", nearby_place.name)

    print()

# =========================
# SIMPLE AI TRAVEL PLANNER
# =========================

print("\n===== SIMPLE AI TRAVEL PLANNER =====\n")

user_place = input("Enter a place name: ")

print("\nRecommended Foods:\n")

found_food = False

for food in onto.Food.instances():

    for place in food.famousin:

        if place.name.lower() == user_place.lower():
            print("-", food.name)
            found_food = True

if not found_food:
    print("No food recommendations found.")

# =========================
# TOURIST PLACE RECOMMENDATION
# =========================

print("\nTourist Places:\n")

found_place = False

for tourist_place in onto.Tourist_Place.instances():

    for place in tourist_place.locatedIn:

        if place.name.lower() == user_place.lower():
            print("-", tourist_place.name)
            found_place = True

if not found_place:
    print("No tourist places found.")

# =========================
# HOTEL RECOMMENDATION
# =========================

print("\nHotels:\n")

found_hotel = False

for hotel in onto.Hotel.instances():

    for nearby_place in hotel.NearTo:

        if nearby_place.name.lower() == user_place.lower():
            print("-", hotel.name)
            found_hotel = True

if not found_hotel:
    print("No hotels found.")

print("\n===== THANK YOU =====")