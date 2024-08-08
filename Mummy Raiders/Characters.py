class Character:
    def __init__(self, name, role, description, bonus):
        self.name = name
        self.role = role
        self.description = description
        self.bonus = bonus

    def get_description(self):
        return f"In front of you is a chracter with role {self.role}. {self.description} Bonus: {self.bonus}"

class Archaeologist(Character):
    name = "Dr. Elias Venturi"
    role = "Archaeologist"
    description = ("""
    Dr. Elias Venturi is a renowned archaeologist from Italy, 
    captivated by the mysteries of ancient civilizations. His expertise in 
    excavation allows him to dig 25% faster than others, giving him a significant edge 
    in uncovering the hidden relics of Ankh-Ra.
    """)
    bonus = "25% faster excavation"
    # def __init__(self, name):
    #     description = ("Dr. Elias Venturi is a renowned archaeologist from Italy, "
    #                    "captivated by the mysteries of ancient civilizations. His expertise in "
    #                    "excavation allows him to dig 25% faster than others, giving him a significant edge "
    #                    "in uncovering the hidden relics of Ankh-Ra.")
    #     bonus = "25% faster excavation"
    #     super().__init__(name=name, role="Archaeologist", description=description, bonus=bonus)
    def excavate(self, time):
        return time * 0.75

class Merchant(Character):
    name = "Samira al-Jaffar"
    role = "Merchant"
    description = """
    Samira al-Jaffar is a seasoned merchant from Cairo, known for her sharp wit and 
    unmatched negotiation skills. Her keen business acumen grants her a 25% bonus on all sales, 
    allowing her to maximize profits from any treasure she uncovers.
    """
    bonus = "25% bonus on all sales"
    # def __init__(self, name):
    #     description = ("""Samira al-Jaffar is a seasoned merchant from Cairo, known for her sharp wit and
    #                    unmatched negotiation skills. Her keen business acumen grants her a 25% bonus on all sales,
    #                    allowing her to maximize profits from any treasure she uncovers.""")
    #     bonus = "25% increased sale value"
    #     super().__init__(name, role="Merchant", description=description, bonus=bonus)
    #
    # def sell(self, base_price):
    #     return base_price * 1.25
    def sell(self, base_price):
        return base_price * 1.25