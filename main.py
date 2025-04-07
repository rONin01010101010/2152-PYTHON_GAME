# Import the random library to use for the dice later
import random
import functions
import os 
import platform
from HeroClass import *
from monsterClass import *
from characterClass import *

print("Python Version:", platform.python_version)

# Loot Rarity Tiers
RARITY_TIERS = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]

# Loot Categories
EQUIPMENT_TYPES = ["Weapon", "Armor", "Boots", "Gloves", "Helmet", "Shield", "Amulet", "Ring"]
CONSUMABLE_TYPES = ["Health Potion", "Mana Potion", "Strength Potion", "Poison Potion", "Elixir"]
JUNK_TYPES = ["Broken Shield", "Rusty Sword", "Tattered Cloth", "Old Boot", "Damaged Helm"]

# Item Database
ITEM_DATABASE = {
    # Common Items
    "Small Health Potion": {"type": "Consumable", "rarity": "Common", "effect": 2, "value": 5, "sellable": True},
    "Leather Boots": {"type": "Equipment", "rarity": "Common", "effect": 1, "value": 10, "equippable": True},
    "Rusty Dagger": {"type": "Equipment", "rarity": "Common", "effect": 1, "value": 8, "equippable": True},
    "Cloth Hood": {"type": "Equipment", "rarity": "Common", "effect": 1, "value": 7, "equippable": True},
    
    # Uncommon Items
    "Health Potion": {"type": "Consumable", "rarity": "Uncommon", "effect": 4, "value": 15, "sellable": True},
    "Iron Sword": {"type": "Equipment", "rarity": "Uncommon", "effect": 3, "value": 25, "equippable": True},
    "Chainmail": {"type": "Equipment", "rarity": "Uncommon", "effect": 2, "value": 30, "equippable": True},
    "Mana Crystal": {"type": "Consumable", "rarity": "Uncommon", "effect": 3, "value": 20, "sellable": True},
    
    # Rare Items
    "Greater Health Potion": {"type": "Consumable", "rarity": "Rare", "effect": 6, "value": 40, "sellable": True},
    "Steel Longsword": {"type": "Equipment", "rarity": "Rare", "effect": 5, "value": 60, "equippable": True},
    "Plated Armor": {"type": "Equipment", "rarity": "Rare", "effect": 4, "value": 75, "equippable": True},
    "Enchanted Amulet": {"type": "Equipment", "rarity": "Rare", "effect": 4, "value": 65, "equippable": True},
    
    # Epic Items
    "Supreme Health Elixir": {"type": "Consumable", "rarity": "Epic", "effect": 10, "value": 90, "sellable": True},
    "Enchanted Blade": {"type": "Equipment", "rarity": "Epic", "effect": 8, "value": 120, "equippable": True},
    "Mystic Shield": {"type": "Equipment", "rarity": "Epic", "effect": 7, "value": 110, "equippable": True},
    
    # Legendary Items
    "Phoenix Feather": {"type": "Consumable", "rarity": "Legendary", "effect": 15, "value": 200, "sellable": True},
    "Dragon's Fang Sword": {"type": "Equipment", "rarity": "Legendary", "effect": 12, "value": 250, "equippable": True},
    "Celestial Armor": {"type": "Equipment", "rarity": "Legendary", "effect": 10, "value": 300, "equippable": True},
    
    # Junk/Bad Items
    "Poison Potion": {"type": "Consumable", "rarity": "Common", "effect": -2, "value": 3, "sellable": True},
    "Broken Shield": {"type": "Junk", "rarity": "Common", "effect": 0, "value": 1, "sellable": True},
    "Tattered Cloth": {"type": "Junk", "rarity": "Common", "effect": 0, "value": 1, "sellable": True},
}

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0




# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Lab 06 - Question 5b
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Lab Week 06 - Question 6
    num_dream_lvls = -1  # Initialize the number of dream levels

while num_dream_lvls < 0 or num_dream_lvls > 3:
    # Prompt the user for input
    print("    |", end="    ")
    user_input = input("How many dream levels do you want to go down? (Enter a number 0-3): ")

    # If the input is an empty string, prompt again
    if user_input == "":
        print("Number entered must be a whole number between 0-3 inclusive, try again")
    else:
        try:
            # Try to convert the input to an integer
            num_dream_lvls = int(user_input)

            # Validate the input to ensure it's between 0 and 3
            if num_dream_lvls < 0 or num_dream_lvls > 3:
                print("Number entered must be a whole number between 0-3 inclusive, try again")
                num_dream_lvls = -1  # Reset to invalid value to continue the loop
            elif num_dream_lvls != 0:
                # Simulate health point and combat strength changes
                health_points -= 1  # Assuming health_points is defined earlier
                # Assuming a function 'inception_dream' affects combat_strength
                crazy_level = functions.inception_dream(num_dream_lvls)
                combat_strength += crazy_level
                print("combat strength: " + str(combat_strength))
                print("health points: " + str(health_points))
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter a whole number between 0-3 inclusive.")
            num_dream_lvls = -1  # Reset to invalid value to continue the loop

# After the loop ends, print the final value of num_dream_lvls
    print("num_dream_lvls: ", num_dream_lvls)
    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                health_points = functions.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                m_health_points = functions.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if(m_health_points <= 0):
        winner = "Hero"
    else:
        winner = "Monster"

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)       


def save_game(hero, monster, monsters_killed):
       with open("game_save.txt", "w") as file:
        file.write(f"Hero Combat Strength: {hero.combat_strength}\n")
        file.write(f"Hero Health Points: {hero.health_points}\n")
        file.write(f"Monster Combat Strength: {monster.combat_strength}\n")
        file.write(f"Monster Health Points: {monster.health_points}\n")
        file.write(f"Monsters Killed: {monsters_killed}\n")  # Save the number of monsters killed
        print("Game saved!")


def load_game():
    try:
        with open("game_save.txt", "r") as file:
            lines = file.readlines()
            
            hero_combat_strength = int(lines[0].split(": ")[1])
            hero_health_points = int(lines[1].split(": ")[1])
            monster_combat_strength = int(lines[2].split(": ")[1])
            monster_health_points = int(lines[3].split(": ")[1])
            
            monsters_killed = int(lines[4].split(": ")[1])  

        hero = Hero()
        hero.combat_strength = hero_combat_strength
        hero.health_points = hero_health_points

        monster = Monster()
        monster.combat_strength = monster_combat_strength
        monster.health_points = monster_health_points

        print(f"Monsters killed so far: {monsters_killed}")
        
        return hero, monster, monsters_killed
    
    except FileNotFoundError:
        print("No previous save found. Starting a new game.")
        return Hero(), Monster(), 0  






# Sara's loot filter feature
def filter_loot(belt):
    """
    Filter loot in the belt based on quality criteria:
    - Keep items with "Potion" in the name
    - Keep items with longer names (suggesting special items)
    - Remove junk items
    """
    filtered_belt = []
    for item in belt:
        if "Potion" in item and "Poison" not in item:
            print(f"    |    Keeping {item} - Good healing item!")
            filtered_belt.append(item)
        elif len(item) > 10:  # Longer named items are usually special
            print(f"    |    Keeping {item} - Looks valuable!")
            filtered_belt.append(item)
        elif item in ITEM_DATABASE and ITEM_DATABASE[item]["type"] != "Junk":
            print(f"    |    Keeping {item} - Might be useful later")
            filtered_belt.append(item)
        else:
            print(f"    |    Discarding {item} - Just junk")
    
    print(f"    |    Filtered belt: {filtered_belt}")
    return filtered_belt

# Kenan's inventory system based on player level
def generate_inventory(player_level):
    """
    Generate inventory capacity and items based on player level:
    - Higher level players get more inventory slots
    - Higher level players find better quality items
    """
    # Determine inventory capacity based on player level
    if player_level >= 5:
        max_capacity = 10
        item_quality = "Legendary"
    elif player_level >= 3:
        max_capacity = 8
        item_quality = "Epic"
    else:
        max_capacity = 5
        item_quality = "Uncommon"
    
    print(f"    |    Player level {player_level}: Inventory capacity is {max_capacity}")
    
    # Generate starter inventory
    inventory = []
    
    # Generate some starter items appropriate for the player's level
    possible_items = [item for item, attrs in ITEM_DATABASE.items() 
                     if RARITY_TIERS.index(attrs["rarity"]) <= RARITY_TIERS.index(item_quality)]
    
    # Add some starter items (fewer than max capacity)
    num_starter_items = min(3, max_capacity - 1)
    for _ in range(num_starter_items):
        if possible_items:
            new_item = random.choice(possible_items)
            inventory.append(new_item)
            
    
    print(f"    |    Starting inventory: {inventory}")
    return {"items": inventory, "capacity": max_capacity}

# Stanley's rarity-based looting system
def generate_monster_loot(monster_level):
    """
    Generate loot from defeated monsters based on their level.
    Higher level monsters drop better loot with increased rarity.
    """
    # Determine potential drop quality based on monster level
    if monster_level >= 5:
        possible_rarities = ["Uncommon", "Rare", "Epic", "Legendary"]
        num_items = random.randint(2, 4)
    elif monster_level >= 3:
        possible_rarities = ["Common", "Uncommon", "Rare"]
        num_items = random.randint(1, 3)
    else:
        possible_rarities = ["Common", "Uncommon"]
        num_items = random.randint(1, 2)
    
    # Small chance for a better rarity item
    if random.random() < 0.1:  # 10% chance for better loot
        if "Legendary" not in possible_rarities:
            possible_rarities.append(RARITY_TIERS[RARITY_TIERS.index(possible_rarities[-1]) + 1])
    
    # Generate loot items
    loot_items = []
    for _ in range(num_items):
        # Select rarity for this item
        rarity = random.choice(possible_rarities)
        
        # Get all items of that rarity
        possible_items = [item for item, attrs in ITEM_DATABASE.items() if attrs["rarity"] == rarity]
        
        if possible_items:
            loot_items.append(random.choice(possible_items))
    
    return loot_items

def process_loot(loot_items, inventory):
    """
    Process loot items and determine if they are equippable or sellable.
    Update inventory accordingly.
    """
    print("    |    Examining monster loot...")
    
    for item in loot_items:
        if item in ITEM_DATABASE:
            item_data = ITEM_DATABASE[item]
            rarity = item_data["rarity"]
            
            # Color-coded rarity messages
            rarity_colors = {
                "Common": "",
                "Uncommon": "⬜ ",
                "Rare": "🟦 ",
                "Epic": "🟪 ",
                "Legendary": "🟨 "
            }
            
            rarity_prefix = rarity_colors.get(rarity, "")
            
            # Check if inventory has space
            if len(inventory["items"]) < inventory["capacity"]:
                inventory["items"].append(item)
                
                # Determine item properties
                if "equippable" in item_data and item_data["equippable"]:
                    print(f"    |    {rarity_prefix}Found {rarity} {item}! Added to inventory. Can be equipped.")
                elif "sellable" in item_data and item_data["sellable"]:
                    print(f"    |    {rarity_prefix}Found {rarity} {item}! Added to inventory. Worth {item_data['value']} gold.")
                else:
                    print(f"    |    {rarity_prefix}Found {rarity} {item}! Added to inventory.")
            else:
                print(f"    |    Found {item}, but your inventory is full! Item dropped.")
    
    return inventory

# Function to use an item from inventory
def use_inventory_item(inventory, item_name, health_points, combat_strength):
    """
    Use an item from the inventory and apply its effects.
    Returns updated health_points and combat_strength.
    """
    if item_name in inventory["items"]:
        # Remove the item from inventory
        inventory["items"].remove(item_name)
        
        if item_name in ITEM_DATABASE:
            item_data = ITEM_DATABASE[item_name]
            
            # Apply effects based on item type
            if item_data["type"] == "Consumable":
                effect = item_data["effect"]
                if "Health" in item_name or "Elixir" in item_name:
                    health_points = min(20, health_points + effect)
                    print(f"    |    Used {item_name} to restore {effect} health. Current HP: {health_points}")
                elif "Strength" in item_name:
                    combat_strength += effect
                    print(f"    |    Used {item_name} to gain {effect} combat strength. Current strength: {combat_strength}")
                elif "Poison" in item_name:
                    health_points = max(0, health_points - abs(effect))
                    print(f"    |    Used {item_name} and took {abs(effect)} damage! Current HP: {health_points}")
            elif item_data["type"] == "Equipment" and item_data.get("equippable", False):
                effect = item_data["effect"]
                combat_strength += effect
                print(f"    |    Equipped {item_name} to gain {effect} combat strength. Current strength: {combat_strength}")
        
        return inventory, health_points, combat_strength
    else:
        print(f"    |    {item_name} not found in inventory!")
        return inventory, health_points, combat_strength

# Function to display inventory with item details
def display_inventory(inventory):
    """Display the current inventory with detailed item information."""
    print("\n" + "="*50)
    print(f"INVENTORY ({len(inventory['items'])}/{inventory['capacity']} slots used)")
    print("="*50)
    
    if not inventory["items"]:
        print("Inventory is empty!")
    else:
        for i, item in enumerate(inventory["items"]):
            if item in ITEM_DATABASE:
                item_data = ITEM_DATABASE[item]
                rarity = item_data["rarity"]
                item_type = item_data["type"]
                value = item_data["value"]
                
                # Get color symbol based on rarity
                rarity_symbols = {
                    "Common": "⚪",
                    "Uncommon": "⚪",
                    "Rare": "🔵",
                    "Epic": "🟣",
                    "Legendary": "🟡"
                }
                
                symbol = rarity_symbols.get(rarity, "⚪")
                
                # Print item with details
                print(f"{i+1}. {symbol} {item} ({rarity} {item_type}) - {value} gold")
                
                # Add extra description based on type
                if "effect" in item_data:
                    effect = item_data["effect"]
                    if item_type == "Consumable":
                        if effect > 0:
                            print(f"   Restores {effect} health/mana when used")
                        else:
                            print(f"   Causes {abs(effect)} damage when used")
                    elif item_type == "Equipment":
                        print(f"   Provides +{effect} to combat strength when equipped")
            else:
                print(f"{i+1}. {item} (Unknown item)")
    
    print("="*50)

# Main function to integrate all loot-related features
def manage_loot_system(player_level, belt, health_points, combat_strength, monster_level=None):
    """Main function to handle all loot-related operations."""
    
    # Initialize or update inventory if needed
    inventory = generate_inventory(player_level)
    
    # Filter existing belt items (Sara's feature)
    filtered_belt = filter_loot(belt)
    
    # Add filtered belt items to inventory
    for item in filtered_belt:
        if len(inventory["items"]) < inventory["capacity"]:
            inventory["items"].append(item)
        else:
            print(f"    |    Couldn't add {item} - inventory full!")
    
    # Generate and process monster loot if monster was defeated (Stanley's feature)
    if monster_level is not None:
        monster_loot = generate_monster_loot(monster_level)
        if monster_loot:
            print(f"    |    Monster dropped {len(monster_loot)} items!")
            inventory = process_loot(monster_loot, inventory)
    
    # Display the complete inventory
    display_inventory(inventory)
    
    return inventory, health_points, combat_strength

class Adventure:
    def __init__(self, hero_name="Adventurer"):
        self.hero_name = hero_name
        self.health_points = 10
        self.combat_strength = 5
        self.m_health_points = 8
        self.m_combat_strength = 3
        self.player_level = 1
        self.belt = ["Health Potion", "Leather Boots", "Rusty Dagger"]
        self.inventory = None
        self.gold = 0
        
        # Welcome banner
        print("\n" + "="*50)
        print(f"WELCOME TO THE ADVENTURE, {self.hero_name.upper()}!")
        print("="*50)
        
        # Initialize inventory system with player's belt items
        self.inventory, self.health_points, self.combat_strength = manage_loot_system(
            self.player_level, self.belt, self.health_points, self.combat_strength)
        
        # Adjust combat strength based on previous games
        functions.adjust_combat_strength(self.combat_strength, self.m_combat_strength)
    
    def explore(self):
        """Player explores and finds loot."""
        print("\n" + "-"*50)
        print("You venture forth into the unknown...")
        
        # Random chance to find a chest
        if random.random() < 0.7:  # 70% chance to find something
            print("You found a treasure chest!")
            # Use Sara's loot filter on found items
            found_items = [random.choice(list(ITEM_DATABASE.keys())) for _ in range(2)]
            filtered_items = filter_loot(found_items)
            
            # Add filtered items to inventory
            for item in filtered_items:
                if len(self.inventory["items"]) < self.inventory["capacity"]:
                    self.inventory["items"].append(item)
                    print(f"    |    Added {item} to your inventory.")
                else:
                    print(f"    |    Found {item}, but your inventory is full! Item dropped.")
        else:
            print("You found nothing of interest.")
        
        # Small chance to encounter a monster
        if random.random() < 0.3:  # 30% chance to encounter monster
            print("\nA monster appears!")
            self.combat()
        
        # Display updated inventory
        display_inventory(self.inventory)
    
    def shop(self):
        """Player visits a shop to buy/sell items."""
        print("\n" + "-"*50)
        print(f"WELCOME TO THE SHOP! You have {self.gold} gold.")
        print("-"*50)
        
        # Display inventory for selling
        print("YOUR INVENTORY:")
        display_inventory(self.inventory)
        
        # Shopping options
        print("\nSHOP OPTIONS:")
        print("1. Sell an item")
        print("2. Buy an item")
        print("3. Leave shop")
        
        choice = input("What would you like to do? (1-3): ")
        
        if choice == "1":  # Sell
            if not self.inventory["items"]:
                print("You have nothing to sell!")
                return
                
            sell_index = input("Enter the number of the item you want to sell (0 to cancel): ")
            if sell_index.isdigit() and int(sell_index) > 0 and int(sell_index) <= len(self.inventory["items"]):
                item_to_sell = self.inventory["items"][int(sell_index) - 1]
                if item_to_sell in ITEM_DATABASE and ITEM_DATABASE[item_to_sell].get("sellable", False):
                    value = ITEM_DATABASE[item_to_sell]["value"]
                    self.inventory["items"].remove(item_to_sell)
                    self.gold += value
                    print(f"Sold {item_to_sell} for {value} gold. You now have {self.gold} gold.")
                else:
                    print("This item cannot be sold.")
        
        elif choice == "2":  # Buy
            # Show shop inventory - only items the player can afford
            print("\nAVAILABLE ITEMS:")
            shop_items = [item for item, data in ITEM_DATABASE.items() 
                        if data["value"] <= self.gold and item not in self.inventory["items"]]
            
            if not shop_items:
                print("Nothing available to buy with your current gold.")
                return
                
            for i, item in enumerate(shop_items):
                data = ITEM_DATABASE[item]
                print(f"{i+1}. {item} - {data['value']} gold ({data['rarity']} {data['type']})")
            
            buy_index = input("Enter the number of the item you want to buy (0 to cancel): ")
            if buy_index.isdigit() and int(buy_index) > 0 and int(buy_index) <= len(shop_items):
                item_to_buy = shop_items[int(buy_index) - 1]
                value = ITEM_DATABASE[item_to_buy]["value"]
                
                if len(self.inventory["items"]) < self.inventory["capacity"]:
                    self.inventory["items"].append(item_to_buy)
                    self.gold -= value
                    print(f"Bought {item_to_buy} for {value} gold. You now have {self.gold} gold.")
                else:
                    print("Your inventory is full! Cannot buy more items.")
    
    def combat(self):
        """Player engages in combat with a monster."""
        monster_level = max(1, self.player_level - 1 + random.randint(0, 2))
        m_health_points = 5 + (2 * monster_level)
        m_combat_strength = 2 + monster_level
        
        print(f"\nYou encounter a Level {monster_level} Monster! (HP: {m_health_points}, Strength: {m_combat_strength})")
        
        # Combat loop
        while self.health_points > 0 and m_health_points > 0:
            print("\nCOMBAT OPTIONS:")
            print("1. Attack")
            print("2. Use Item")
            print("3. Run Away")
            
            action = input("What would you like to do? (1-3): ")
            
            if action == "1":  # Attack
                # Player attacks monster
                m_health_points = functions.hero_attacks(self.combat_strength, m_health_points)
                
                # If monster defeated
                if m_health_points <= 0:
                    print("You defeated the monster!")
                    experience_gain = 10 * monster_level
                    gold_gain = 5 * monster_level
                    self.gold += gold_gain
                    print(f"You gained {experience_gain} experience and {gold_gain} gold!")
                    
                    # Level up check - simple system
                    if experience_gain > 20 and self.player_level < 5:
                        self.player_level += 1
                        self.combat_strength += 1
                        print(f"LEVEL UP! You are now level {self.player_level}!")
                    
                    # Get loot from monster (Stanley's feature)
                    self.inventory, self.health_points, self.combat_strength = manage_loot_system(
                        self.player_level, [], self.health_points, self.combat_strength, monster_level)
                    
                    # Save game result
                    functions.save_game("Hero", self.hero_name, monster_level)
                    break
                
                # Monster attacks player
                self.health_points = functions.monster_attacks(m_combat_strength, self.health_points)
                
                # If player defeated
                if self.health_points <= 0:
                    print("You were defeated!")
                    functions.save_game("Monster")
                    break
            
            elif action == "2":  # Use Item
                display_inventory(self.inventory)
                item_choice = input("Enter item number to use (0 to cancel): ")
                
                if item_choice.isdigit() and int(item_choice) > 0 and int(item_choice) <= len(self.inventory["items"]):
                    item_to_use = self.inventory["items"][int(item_choice) - 1]
                    self.inventory, self.health_points, self.combat_strength = use_inventory_item(
                        self.inventory, item_to_use, self.health_points, self.combat_strength)
                    
                    # Monster still gets to attack
                    if m_health_points > 0:
                        self.health_points = functions.monster_attacks(m_combat_strength, self.health_points)
                    
                    # If player defeated
                    if self.health_points <= 0:
                        print("You were defeated!")
                        functions.save_game("Monster")
                        break
            
            elif action == "3":  # Run Away
                escape_chance = 0.5  # 50% chance to escape
                if random.random() < escape_chance:
                    print("You managed to escape!")
                    break
                else:
                    print("You failed to escape!")
                    # Monster gets a free attack
                    self.health_points = functions.monster_attacks(m_combat_strength, self.health_points)
                    
                    # If player defeated
                    if self.health_points <= 0:
                        print("You were defeated!")
                        functions.save_game("Monster")
                        break
    
    def rest(self):
        """Player rests to recover health."""
        heal_amount = min(5, 20 - self.health_points)  # Max health is 20
        if heal_amount > 0:
            self.health_points += heal_amount
            print(f"\nYou rest and recover {heal_amount} health. Current HP: {self.health_points}")
        else:
            print("\nYou are already at full health!")
    
    def game_loop(self):
        """Main game loop."""
        while self.health_points > 0:
            print("\n" + "="*50)
            print(f"{self.hero_name} (Level {self.player_level}) | HP: {self.health_points} | Gold: {self.gold}")
            print("="*50)
            print("\nWhat would you like to do?")
            print("1. Explore")
            print("2. Visit Shop")
            print("3. Rest")
            print("4. Check Inventory")
            print("5. Quit Game")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.shop()
            elif choice == "3":
                self.rest()
            elif choice == "4":
                display_inventory(self.inventory)
            elif choice == "5":
                print("\nThanks for playing!")
                break
            else:
                print("Invalid choice. Try again.")
                
            # Check if player died
            if self.health_points <= 0:
                print("\nGAME OVER! You have been defeated.")
                restart = input("Would you like to start a new adventure? (y/n): ")
                if restart.lower() == "y":
                    self.__init__(self.hero_name)  # Reset the game
                else:
                    print("\nThanks for playing!")
                    break


if __name__ == "__main__":
    hero_name = input("Enter your hero's name: ")
    game = Adventure(hero_name)
    game.game_loop()












os_name = os.name;
print("The operating system is:", os_name)


