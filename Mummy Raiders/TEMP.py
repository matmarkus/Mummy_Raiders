def next_step():
    walidacja = False
    next_step_description = """
    The sun rises on the Nile. Another busy day ahead of you. You look around the area and start looking for where you can stick a shovel today.
Your next step:
1. You start searching the location and rely on intuition. (May take from 1 to 4 hours).
2. You use a map you bought from a mysterious merchant at a market in Cairo. (It will take 2 hours)
    """
    print(next_step_description)
    next_step_decision = input("So what do you choose? Option 1 or 2? ")
    if next_step_decision == "1":
        #TODO
    elif next_step_decision == "2":
        #TODO
    else print("Invalid choice. Please write down '1'or '2'")
        return next_step_decision