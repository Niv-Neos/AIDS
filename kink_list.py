### This is to allow engine stats to be placed on Kinks :3
Traits = []

def debug_info():
    print("Number of objects on each list")
    print("==============================")
    print("Gender: ", len(gender))
    print("Action List: ", len(action_list))
    print("Mind Control: ", len(mind_control_list))
    print("Goals List: ", len(goals_list))
    print("Dungeon List: ", len(dungeon_list))
    print("Wilds List: ", len(wilds_list))
    print("Creature List:", len(creature_list))
    print("Traps List:", len(traps_list))
    print("Memetic List:", len(memetic_list))
    print("Transformation List:", len(transformation_list))
    print("Defeat List:", len(defeat_list))
    print("==============================")
    '''
    print("Kink list Quicky")
    print("S Tier: ", len(quick_list_s))
    print("A Tier: ", len(quick_list_a))
    print("B Tier: ", len(quick_list_b))
    print("C Tier: ", len(quick_list_c))
    print("D Tier: ", len(quick_list_d))
    print("E Tier: ", len(quick_list_e))
    print("F Tier: ", len(quick_list_f))
    '''

def all_list(lister):
    result = 0
    for i in range (0, len(lister)):
        result = result + len(lister[i])
    return result

def ratio_to_database(stringer, lister):
    total = all_list(lister)
    result = 0
    for i in range (0, len(lister)-1):
        for x in range (0, len(lister[i])-1):
            if stringer in lister[i][x][2][0]:
                result = (result*lister[i][x][2][1]) + 1
    return ((result/total)*100,"%")

def ifelse(ifstate, elsestate, condition):
    if condition in Traits:
        return ifstate
    else:
        return elsestate

def OrCheck(lister):
    for i in range(0,len(lister)):
        if i in Traits:
            return i
        else:
            return 0

### [Name, Normal?]
gender = [
    ["Fale", 1],
    ["Male", 1],
    ["Herm", 0],
    ["No Gender", 0]
]

### [Name, Kinkable, Ratio to Database]
genre = [
    ["Fantasy", 100],
    ["Sci-fi", 85],
    ["Horror", 95],
    ["Fighter", 25],
    ["Spies", 35]
    ]

### [Name, Gender Exlusiion [], Genre Exlusion [], Popularity int 0/100
theme = [
    ["Fantasy", [0], [genre[0], genre[1]], 100],
    ["Chase", [0], None, 70],
    ["Dungeon Crawl", [0], [genre[0]], 100],
    ["Survival", [0], None, 95],
    ["Stalked", [0], None, 50],
    ["Escape", [0], [genre[0], genre[1], genre[2]], 75],
    ["War", [0], None, 10],
    ["Other", [0], None, 1]
]

### [Name, Gender Exlusiion [], Genre Assocation {[],%}, Theme Assocation []]

goals_list = [
    [  ["Breed"], [ gender[0], gender[1], gender[2] ], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 2 ], [0]  ],
    [  ["Enslave"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 2 ], [0]  ],
    [  ["Eat"], [0], [ ["Fantasy", "Sci-fi"], 1.5 ], [0]  ],
    [  ["Rape"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 3 ], [0]  ],
    [  ["Pet"], [0], [ ["Fantasy", "Sci-fi", "Fighter"] , 1 ], [0]  ],
    [  ["Milker"], [ gender[0], gender[2] ], [ ["Fantasy", "Sci-fi", "Spies"] , 2 ], [0]  ],
    [  ["Cattle"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Trophy"], [0], [ ["Fantasy", "Fighter"] , 0.1 ], [0]  ],
    [  ["Play"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.1 ], [0]  ],
    [  ["Fight"], [0], [ ["Fighter"] , 2 ], [0]  ],
    [  ["Teach a Lession"], [0], [ ["Fighter"] , 0.1 ], [0]  ],
    [  ["Extract"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.5 ], [0]  ],
    [  ["Feed"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 1.5 ], [0]  ],
    [  ["Inject"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.25 ], [0]  ],
    [  ["Infect"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.25 ], [0]  ],
    [  ["Transform"], [0], [ ["Fantasy", "Horror", "Spies"] , 0.5 ], [0]  ],
    [  ["Experiment"], [0], [ ["Fantasy", "Sci-fi"], 0.75 ], [0]  ]
]

memetic_list = [
    [  ["Sexism"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Specism"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Slavery"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Kidnapping"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Brooding"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Invasion"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 0.5 ], [0]  ],
    [  ["Defending"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 0.5 ], [0]  ],
    [  ["Experimenting"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , ifelse(2, 0.5, OrCheck([goals_list[15]])) ], [0]  ],
    [  ["Observing"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Harassing"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Arcane Usage"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Questioning"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Breeding"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , ifelse(2, 0.25, OrCheck([goals_list[0]])) ], [0]  ],
    [  ["Spying"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Crime"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Submissive"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Adoring"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Lusting"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Dominating"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ]
]

dungeon_list = [
    [  ["Dungeon"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Factory"], [0], [ ["Sci-fi", "Fighter"] , 1 ], [0]  ],
    [  ["Temple"], [0], [ ["Fantasy"], 1.25 ], [0]  ],
    [  ["Mansion"], [0], [ ["Horror", "Mansion"] , 2 ], [0]  ],
    [  ["Lab"], [0], [ ["Sci-fi"] , 2 ], [0]  ],
    [  ["Fortress"], [0], [ ["Sci-fi", "Fighter", "Fortress"], 1.5 ], [0]  ],
    [  ["Farm"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"], 0.75 ], [0]  ],
    [  ["City"], [0], [ ["Sci-fi", "Fighter", "Spies"], 1.15], [0]  ],
    [  ["Garden"], [0], [ ["Fantasy", "Horror"], 0.5 ], [0]  ],
    [  ["Park"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Camp"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Sewer"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Underground"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Castle"], [0], [ ["Fantasy", "Horror"] , 1 ], [0]  ],
    [  ["Hive"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Sea"], [0], [ ["Fantasy", "Sci-fi"] , 0.5 ], [0]  ]
]
wilds_list = [
    [  ["Agricultural land"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Woodland"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Forest"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Jungle"], [0], [ ["Fantasy", "Sci-fi"] , 2 ], [0]  ],
    [  ["Mountain"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 1 ], [0]  ],
    [  ["Valley"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Desert"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Grassland"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Sewer"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Abyss"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Island"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ]
]
creature_list = [
    [  ["Arthropod"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Bat"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Bird"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Canines"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Feline"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Fish"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Hyena"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Primate"], [0], [ ["Fantasy", "Sci-fi", "Fighter", "Spies"], 0.9 ], [0]  ],
    [  ["Raccoon"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Rabbit"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Reptile"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Rodent"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Vampire"], [0], [ ["Fantasy", "Horror"] , 1 ], [0]  ],
    [  ["Hydra"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Dragon"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Basilisk"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Slime"], [0], [ ["Fantasy", "Sci-fi"] , 2 ], [0]  ],
    [  ["Flower"], [0], [ ["Fantasy", "Sci-fi"] , 2 ], [0]  ],
    [  ["Griffin"], [0], [ ["Fantasy"], 0.5 ], [0]  ],
    [  ["Minotaur"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Demon"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Goblin"], [0], [ ["Fantasy"] , 2 ], [0]  ],
    [  ["Gnomes"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Ogre"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Parasite"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Human"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"], 1.5 ], [0]  ],
    [  ["Slug"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Pig"], [0], [ ["Fantasy", "Horror"] , 1 ], [0]  ],
    [  ["Robot"], [0], [ ["Sci-fi"] , 2 ], [0]  ],
    [  ["Sea Creature"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Forest Creature"], [0], [ ["Fantasy", "Sci-fi"], 1 ], [0] ],
    [  ["Spider"], [0], [ ["Fantasy"], 1.01 ], [0] ]
]

action_list = [
    [  ["Make Up"] , [0], [ ["Fantasy", "Fighter", "Spies"] , 1 ] , [0]  ],
    [  ["Bearhug"] , [0], [ ["Fighter"] , 1 ] , [0]  ],
    [  ["Pin"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 3 ] , [0]  ],
    [  ["Penetrate Throat"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Forced Handjob"], [ gender[1], gender[2] ], [ ["Fantasy", "Sci-fi", "Spies"] , 1 ], [0]  ],
    [  ["Inpreganate"], [0], [ ["Fantasy", "Fighter"] , ifelse(0.75, 0.25, gender[0]) ], [0]  ],
    [  ["Abuse"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.78 ], [theme[4]]  ],
    [  ["Anal Fist"], [0], [ ["Fantasy"] , 0.05 ], [0]  ],
    [  ["Breast Grab"], [ gender[0], gender[2] ], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 0.8 ], [0]  ],
    [  ["Choke"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.8 ], [0]  ],
    [  ["Sit"], [0], [ ["Fantasy", "Fighter", "Spies"] , 0.5 ], [0]  ],
    [  ["Gags"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Whip"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , ifelse(1.25, 0.75, OrCheck([goals_list[1], goals_list[9], goals_list[10], creature_list[17], creature_list[31]])) ], [0]  ],
    [  ["Licking"], [0], [ ["Fantasy", "Sci-fi"] , 0.25 ], [0]  ],
    [  ["Grab"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1.25 ], [0]  ],
    [  ["Slab"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1.25 ], [0]  ],
    [  ["Slash"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Pee On"], [0], [ ["Fantasy", "Sci-fi"] , 0.05 ], [theme[0], theme[3]]  ],
    [  ["Vomit"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , ifelse(0.75, 0.1, OrCheck([dungeon_list[0], dungeon_list[11], dungeon_list[12], wilds_list[2], wilds_list[3], wilds_list[9]])) ], [ theme[0], theme[3] ]  ],
    [  ["Jump On"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Groin Grab"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Slab"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1.25 ], [0]  ],
    [  ["Spray"], [0], [ ["Fantasy", "Sci-fi"] , 0.75 ], [0]  ],
    [  ["Electricute"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 0.1 ], [0]  ],
    [  ["Force Cloth"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.5 ], [theme[1], theme[5]]  ],
    [  ["Spit On"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Slimeる"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1.25 ], [0]  ],
    [  ["Bite"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Spit Attack"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Suck"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Shallow"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , ifelse(1, 0.1, OrCheck([creature_list[0], creature_list[5], creature_list[10], creature_list[16], creature_list[17], creature_list[29]])) ], [0]  ],
    [  ["Trip"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Thrust"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Yell"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 1 ], [0]  ],
    [  ["Sneak Up"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Bondage"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 2 ], [0]  ],
    [  ["Slam"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 0.9 ], [0]  ],
    [  ["Punch"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , ifelse(1.5, 0.75, genre[3]) ], [0]  ],
    [  ["Kick"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , ifelse(1.5, 0.75, genre[3]) ], [0]  ],
    [  ["Infect"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.5 ], [0]  ],
    [  ["Latch On"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 0.75 ], [0]  ],
    [  ["Eat"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Tie Up"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Constrict"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Telekenesis"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Subdue"], [0], [ ["Fantasy", "Sci-fi", "Spies"] , 0.25 ], [0]  ],
    [  ["Arcane"], [0], [ ["Fantasy"] , 1 ], [0]  ],
]    

mind_control_list = [
    [  ["Hypnosis"] , [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Pheromones"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Virus"], [0], [ ["Horror"] , 1 ], [0]  ],
    [  ["Parasite"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Smell"], [0], [ ["Fantasy", "Sci-fi"] , 0.5 ], [0]  ],
    [  ["Brainwash"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter"] , 1 ], [0]  ],
    [  ["Charm"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Suggestion"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 0.5 ], [0]  ],
    [  ["Intimidated"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ]
]

traps_list = [
    [  ["Pitfall"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["pressure plate that shoots an object straight up"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Trip Wire"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"] , 1 ], [0]  ],
    [  ["Gas Spray"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Flower"], [0], [ ["Fantasy", "Sci-fi"] , 2 ], [0]  ],
    [  ["Mummfication"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Tentacles"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Spies"], 3 ], [0]  ],
    [  ["Hypono"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Encase"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Cocoon"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , 1 ], [0]  ],
    [  ["Spray"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Pheromones"], [0], [ ["Fantasy", "Sci-fi"] , 1 ], [0]  ],
    [  ["Vore"], [0], [ ["Fantasy", "Sci-fi", "Horror"], 3 ], [0]  ]
]

transformation_list = [
    [  ["Genderbend"], [gender[0], gender[1]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Herminatize"], [gender[0], gender[1]], [ ["Fantasy"] , 0.75 ], [0]  ],
    [  ["Hyper Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1.5 ], [0]  ],
    [  ["Hyper Belly"], [gender[0], gender[2]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Hyper Butt"], [0], [ ["Fantasy"] , 0.5 ], [0]  ],
    [  ["Polymorph Species"], [gender[0], gender[2]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Hyper Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Weight Gain"], [0], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Multiple Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Lost of Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1 ], [0]  ],
    [  ["Enlarged Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1.25 ], [0]  ],
    [  ["Enlarged Breasts"], [gender[0], gender[2]], [ ["Fantasy"] , 1.5 ], [0]  ],
    [  ["Hyper Penis"], [gender[1], gender[2]], [ ["Fantasy"] , 1.25 ], [0]  ],
]

defeat_list = [
    [  ["Beaten Up"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Killed"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 0.1 ], [0]  ],
    [  ["Captured"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 2 ], [0]  ],
    [  ["Charmed"], [0], [ ["Fantasy", "Sci-fi", "Spies"] , 1 ], [0]  ],
    [  ["Sickness"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , ifelse(1, 0.5, OrCheck([theme[2], theme[3]])) ], [0]  ],
    [  ["Exhaustion"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Convinced"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Surrender"], [0], [ ["Fantasy", "Sci-fi", "Horror", "Fighter", "Spies"] , 1 ], [0]  ],
    [  ["Mind Controlled"], [0], [ ["Fantasy", "Sci-fi", "Spies"] , 1 ], [0]  ],
    [  ["Eaten"], [0], [ ["Fantasy", "Sci-fi", "Horror"] , ifelse(1.75, 0.1, OrCheck([creature_list[0], creature_list[5], creature_list[10], creature_list[16], creature_list[17], creature_list[29]])) ], [0]  ]
]

### Notes The difference between Enlarge and Hyper is that hyper is incapacitating while enlarge is just bulky

kink_list_of_lists = [
    action_list,
    mind_control_list,
    goals_list,
    dungeon_list,
    wilds_list,
    creature_list,
    traps_list,
    memetic_list,
    transformation_list,
    defeat_list
]

quick_list_s = ["Being an Incubator", " Bondage", " Dignity Lost", " Embarrassment", " Power Play (Being Sub)", " Subjection",
" Kidnapping", " Being Marked", " Slavery", " Resistance", " Brat", " Game Over"]
quick_list_a = ["Gaining Lust from External Sources", " Farmed", " In the Wild", " Jungle",
" Nudity Outside of Sex that Can’t be Helped (Often Stripped Naked Whatever for Stealing or What Else)", " Pheromones", " Pregnancy",
" Slime", " Stigma", " Weakening", " Sexism", " Trophy Wife", " Female to Futa", " Male Pregnancy", " Uncontrollable masturbation",
" Overbloated parts to a point of unable to move."]
quick_list_b = ["Wearing Impractical Beautiful Clothing Such as Dressing", " Butt Slapping", " Cat Calling", " Force Feeding",
" Sex Toys", " Spiders and Webbing", " Being a Maid", " Sinking", " Dirt that slow me down."]
quick_list_c = ["Addiction", " Choking", " Encasement", " Force Defecation", " Getting Genital Sucking", " Gags", " Gang Rape",
"Mind Control", " Overlarge Body Parts That Can’t be Moved", " Ryona", " Transformation", " Underwater", " Vore"]
quick_list_d = ["Fungus Growth", " Messiness"]
quick_list_e = ["Breath Play", " Exhibitionism", " Foot Fetish", " Voyeurism", " Piss and Scat"]
quick_list_f = ["Gore", " Farting", " Toilet", " Genital Torture", " Age Play", " Oral"]

debug_info()
'''
for x in range(0,6):
    print(len(action_list[x]))
'''