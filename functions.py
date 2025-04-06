# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")
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




def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")

# Lab 06 - Question 5a
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                print(last_line)
                return last_line
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


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