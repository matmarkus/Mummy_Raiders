locations = [
    {
        "Name": "Ancient Temple",
        "Description": "A sunken temple full of puzzles and traps.",
        "Excavation Time (hours)": 6,
        "Used": False,
    },
    {
        "Name": "Lost City",
        "Description": "Ruins of a forgotten city buried deep in the jungle.",
        "Excavation Time (hours)": 8,
        "Used": False,
    }
]


for location in locations:
    print(f"Location: {location['Name']}")
    print(f"Description: {location['Description']}")
    print(f"Time required: {location['Excavation Time (hours)']} hours")
    print(f"Already used: {'Yes' if location['Used'] else 'No'}")
    print("-" * 40)