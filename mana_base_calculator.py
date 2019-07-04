# format of lands is (name, (colors added), rank, (tags))
lands = [
    ("Azorius Chancery", ("W", "U"), 5, ()),
    ("Azorius Guildgate", ("W", "U"), 8, ()),
    ("Blast Zone", ("C"), 12, ("boardwipe", "counters")),
    ("Blighted Gorge", ("C"), 12, ("burn")),
    ("Blossoming Sands", ("W", "G"), 7, ("lifegain")),
    ("Boros Guildgate", ("W", "R"), 8, ()),
    ("Bountiful Promenade", ("W", "G"), 3, ()),
    ("Cave of Temptation", ("C", "F"), 9, ("counters")),
    ("Cinder Barrens", ("B", "R"), 8, ()),
    ("Clifftop Retreat", ("W", "R"), 3, ()),
    ("Crumbling Necroplis", ("U", "B", "R"), 5, ()),
    ("Crumbling Vestige", ("C"), 11, ()),
    ("Desert of the Fervent", ("R"), 6, ("draw")),
    ("Desert of the True", ("W"), 6, ("draw")),
    ("Detection Tower", ("C"), 12, ("target")),
    ("Dimir Guildgate", ("U", "B"), 8, ()),
    ("Dragonskull Summit", ("B", "R"), 3, ()),
    ("Drowned Catacomb", ("U", "B"), 3, ()),
    ("Emergence Zone", ("C"), 12, ("flash")),
    ("Endless Sands", ("C"), 12, ("exile", "creature")),
    ("Evolving Wilds", ("T", "A"), 1, ()),
    ("Fertile Thicket", ("G"), 10, ()),
    ("Field of Ruin", ("C"), 12, ("destroy", "fetch")),
    ("Flooded Strand", ("T", "W", "U"), 1, ()),
    ("Forgotten Cave", ("R"), 6, ("draw")),
    ("Forsaken Sanctuary", ("W", "B"), 8, ()),
    ("Foul Orchard", ("B", "G"), 8, ()),
    ("Frostwalk Bastion", ("C"), 12, ("creature_land", "snow")),
    ("Gateway Plaza", ("A"), 5, ()),
    ("Golgari Guildgate", ("B", "G"), 8, ()),
    ("Golgari Rot Farm", ("B", "G"), 5, ()),
    ("Grixis Panorama", ("T", "C", "U", "B", "R"), 5, ()),
    ("Gruul Guildgate", ("R", "G"), 8, ()),
    ("Hall of Heliod's Generosity", ("C"), 12, ("enchantment")),
    ("Highland Lake", ("U", "R"), 8, ()),
    ("Hinterland Harbor", ("U", "G"), 3, ()), 
    ("Interplanar Beacon", ("C"), 11, ("planeswalker")),
    ("Izzet Boilerworks", ("U", "R"), 5, ()),
    ("Izzet Guildgate", ("U", "R"), 8, ()),
    ("Jungle Hollow", ("B", "G"), 7, ("lifegain")),
    ("Looming Spires", ("R"), 10, ("combat")),
    ("Luxury Suite", ("B", "R"), 3, ()),
    ("Meandering River", ("W", "U"), 8, ()),
    ("Memorial to Folly", ("W"), 10, ("graveyard")),
    ("Memorial to Glory", ("B"), 10, ("tokens")),
    ("Morphic Pool", ("U", "B"), 3, ()),
    ("Mortuary Mire", ("B"), 10, ("graveyard")),
    ("Mystic Monastery", ("W", "U", "R"), 5, ()),
    ("Orzhov Basilica", ("W", "B"), 5, ()),
    ("Orzhov Guildgate", ("W", "B"), 8, ()), 
    ("Port Town", ("W", "U"), 4, ()),
    ("Radiant Fountain", ("C"), 12, ("lifegain")),
    ("Rakdos Guildgate", ("B", "R"), 8, ()),
    ("River of Tears", ("U", "B"), 8, ()),
    ("Rootbound Crag", ("R", "G"), 3, ()),
    ("Rugged Highlands", ("R", "G"), 7, ("lifegain")),
    ("Rupture Spire", ("A"), 5, ()),
    ("Sacred Foundry", ("W", "R"), 2, ()),
    ("Sandstone Bridge", ("W"), 10, ("combat")),
    ("Scoured Barrens", ("W", "B"), 7, ("lifegain")),
    ("Sea of Clouds", ("W", "U"), 3, ()),
    ("Selesnya Guildgate", ("W", "G"), 8, ()),
    ("Sequestered Stash", ("C"), 12, ("artifact", "graveyard")),
    ("Simic Guildgate", ("U", "G"), 8, ()),
    ("Skyline Cascade", ("B"), 10, ("tap")),
    ("Smoldering Spires", ("R"), 10, ("combat")),
    ("Spawning Bed", ("C"), 12, ("sacrifice", "token")), 
    ("Steam Vents", ("U", "R"), 2, ()),
    ("Stomping Grounds", ("R", "G"), 2, ()),
    ("Stone Quarry", ("W", "R"), 8, ()),
    ("Submerged Boneyard", ("U", "B"), 8, ()),
    ("Sulfur Falls", ("U", "R"), 3, ()),
    ("Sunpetal Grove", ("W", "G"), 3, ()),
    ("Survivors' Encampment", ("C"), 9, ("tap")),
    ("Swiftwater Cliffs", ("U", "R"), 7, ("lifegain")),
    ("Temple Garden", ("W", "G"), 2, ()),
    ("Temple of Abandon", ("G", "R"), 4, ()),
    ("Temple of Epiphany", ("U", "R"), 4, ()),
    ("Timber Gorge", ("R", "G"), 8, ()),
    ("Tranquil Cove", ("W", "U"), 7, ("lifegain")),
    ("Tranquil Expanse", ("W", "G"), 8, ()),
    ("Unclaimed Territory", ("C"), 11, ("tribal")),
    ("Unknown Shores", ("C", "F"), 9, ()),
    ("Watery Grave", ("U", "B"), 2, ()),
    ("Woodland Cemetery", ("B", "G"), 3, ()),
    ("Woodland Stream", ("U", "G"), 8, ())
]
available_lands = []
basics = {
    "W":"Plains",
    "U":"Island",
    "B":"Swamp",
    "R":"Mountain",
    "G":"Forest"
}

colors_temp = raw_input("Enter needed colors capitalized with spaces (EX: R W B):")
colors = colors_temp.split()
color_balance = {}
for c in colors:
    print "How many color symbols for %r?" % c
    color_balance.update({c: int(raw_input())})

tags_temp = raw_input("Enter needed special categories with spaces (EX: lifegain tribal artifact tap):")
tags = tags_temp.split()

# this section determines which lands can actually be used based on colors
if len(colors) == 1:
    for i in colors:
        for j in lands:
            if (i in j[1]) and (len(j[1]) == 1):
                available_lands.append(j)

if len(colors) == 2:
    for j in lands:
        if ((colors[0] in j[1]) and (colors[1] in j[1])) and (len(j[1]) == 2):
            available_lands.append(j)
        elif ((colors[0] in j[1]) or (colors[1] in j[1])) and (len(j[1]) == 1):
            available_lands.append(j)

if len(colors) == 3:
    for j in lands:
        if ((colors[0] in j[1]) and (colors[1] in j[1]) and (colors[2] in j[1])) and (len(j[1]) == 3):
            available_lands.append(j)
        if ((colors[0] in j[1]) and (colors[1] in j[1])) and (len(j[1]) == 2):
            available_lands.append(j)
        if ((colors[1] in j[1]) and (colors[2] in j[1])) and (len(j[1]) == 2):
            available_lands.append(j)
        if ((colors[0] in j[1]) and (colors[2] in j[1])) and (len(j[1]) == 2):
            available_lands.append(j)
        elif ((colors[0] in j[1]) or (colors[1] in j[1]) or (colors[2] in j[1]) or ("A" in j[1])) and (len(j[1]) == 1):
            available_lands.append(j)

if len(colors) == 4:
    lands_temp = []
    available_lands = lands
    for i in ["W", "U", "B", "R", "G", "C"]:
        if i not in colors:
            for j in lands:
                if i in j[1]:
                    lands_temp.append(j)
    for i in lands_temp:
        available_lands.remove(i)        

if len(colors) == 5:
    available_lands = lands

if (len(colors) >= 2) and (("Evolving Wilds", ("T", "A"), 1, ()) not in available_lands):
    available_lands.append(("Evolving Wilds", ("T", "A"), 1, ()))

# this section determines the best mix of those lands
lands_final = []
weight = 0
number = 0
for n in range(1, 13):
    for j in available_lands:
        add_land = True
        if (number >= 20) or (weight >= 100): 
            add_land = False
        for c in color_balance.keys():
            if (color_balance.get(c) < 1) and (c in j[1]):
                add_land = False
        if n == j[2]:
            if add_land:
                lands_final.append(j)
                weight += n
                number +=1
                for c in color_balance.keys():
                    if c == "A":
                        for c in color_balance.keys():
                            color_balance.update({c: (color_balance[c] - 1)})
                    elif c in j[1]:
                        color_balance.update({c: (color_balance[c] - 1)})
    
# this section adds needed tagged lands
colors.append("C")
for i in tags:
    for j in lands:
        if i in j[3]:
            in_color = True
            for c in j[1]:
                if c not in colors:
                    in_color = False
            if (in_color == True) and (j not in lands_final):
                lands_final.append(j)

# this section adds basics to fill in the rest
how_many_basics = int(raw_input("How many lands total?")) - len(lands_final)
basics_list = {}
basic_balance = {}
total_symbols = 0
for c in color_balance.keys():
    basics_list.update({basics.get(c) : 1})
    color_balance.update({c: (color_balance[c] - 1)})
    how_many_basics -= 1
    total_symbols += color_balance[c]
for c in color_balance.keys():
    if color_balance[c] > 0:
        basic_balance.update({c : round(1.0 * color_balance[c] / total_symbols * how_many_basics)})
for c in basic_balance.keys():
    basics_list.update({basics.get(c) : 1 + basic_balance[c]})


# this prints the list of lands
for i in lands_final:
    print i[0]

for i in basics_list.keys():
    print int(basics_list[i]), i