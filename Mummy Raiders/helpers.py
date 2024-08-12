import random
from config import TIME
from Locations import locations

def background_story():
    from ASCII import pyramides
    game_background = """
    In the 1920s, the allure of Egypt's untapped mysteries draws adventurers, scholars, and treasure seekers from across the globe. 
    You are among them, captivated by legends of Ankh-Ra, a lost city buried beneath the desert sands, said to hold untold wealth and forgotten knowledge.

    According to ancient texts, Ankh-Ra was once a thriving hub of power and magic, ruled by a mysterious pharaoh whose name has been erased from history. 
    The city vanished suddenly, leaving behind nothing but whispers of a dark curse and a forgotten civilization.

    Driven by curiosity and the promise of adventure, you set out to uncover the secrets of Ankh-Ra. But as you delve deeper into its ruins, you find that the path ahead is filled with unexpected challenges. 
    Ancient traps, cryptic puzzles, and forces beyond comprehension stand in your way. The desert holds more than just the remains of a forgotten city – it hides dangers that defy reason and twist reality.

    With every step, the line between legend and truth blurs, forcing you to rely on your wits, courage, and perhaps a bit of luck. As the sands shift and shadows lengthen, one question remains: 
    Will you emerge from Ankh-Ra with its secrets, or will the desert claim you as it has countless others before?
    """
    print(pyramides)
    print(game_background)

def round_to_quarter(value):
    return round(value * 4) / 4

def next_step():
    global TIME
    while True:
        next_step_description = """
        The sun rises on the Nile. Another busy day ahead of you. You look around the area and start looking for where you can stick a shovel today.
        Your next step:
        1. You start searching the location and rely on intuition. (May take from 1 to 4 hours).
        2. You use a map you bought from a mysterious merchant at a market in Cairo. (It will take 2 hours)
        """
        print(next_step_description)
        next_step_decision = input("So what do you choose? Option 1 or 2? ")
        if next_step_decision == "1":
            random_hours = random.randint(1, 4)
            TIME += random_hours
            TIME = round_to_quarter(TIME)
            print(f"You relied on intuition. It took {random_hours} hours. New TIME: {TIME}")
            break
        elif next_step_decision == "2":
            TIME += 2
            TIME = round_to_quarter(TIME)
            print(f"You used the map. It took 2 hours. New TIME: {TIME}")
            break
        else:
            print("Invalid choice. Please write down '1' or '2'")

def choosing_difficulty():
    walidacja = False
    while not walidacja:
        difficulty = input("""
        Now it's time to choose your difficulty level:
        >Easy (type in 'E')
        >Medium (type in 'M')
        >Hard (type in 'H')
         -->
        """).upper()
        if difficulty == 'E':
            print("<-----><-----><----->")
            print("You will play on Easy settings!")
            with open("chosen_difficulty.txt", "w") as file:
                file.write("E")
            walidacja = True
        elif difficulty == 'M':
            print("<-----><-----><----->")
            print("You will play on Medium settings!")
            with open("chosen_difficulty.txt", "w") as file:
                file.write("M")
            walidacja = True
        elif difficulty == 'H':
            print("<-----><-----><----->")
            print("You will play on Hard settings!")
            with open("chosen_difficulty.txt", "w") as file:
                file.write("H")
            walidacja = True
        else:
            print("Invalid choice. Please write down 'E', 'M' or 'H'")
            walidacja = False
    return walidacja

def get_random_location(locations):
    unused_locations = [location for location in locations if not location["Used"]]
    if not unused_locations:
        return None
    selected_location = random.choice(unused_locations)
    selected_location["Used"] = True
    return selected_location

def random_location_output(random_location, time_per_day, TIME):
    """gives info about new location"""
    if random_location:
        print(f"Your location: {random_location['Name']}.")
        print(f"Description: {random_location['Description']}")
        remaining_time = time_per_day - TIME
        print(f"Your remaining time for today is {remaining_time}")
    else:
        print("ERROR ERROR ERROR!")
