def defeat_monsters_in_dungeon():
    dungeon = [
        "Goblin", 
        "Gold coins", 
        "Dragon",
        "Dragon",
        "Bandit",
        "Gold coins",
        "Giant Snake"]
    # Your code goes here...
    for i in range((len(dungeon))):
        dungeon[i] = "Gold coins"
        i += 1
        
    return dungeon