import math as mt
import random as rd
import kink_list as kl
import time as ti
import config as cf

danger_encounters = 0
debug = 0
version_i = 2 ### Edition
version_ii = 1 ### Version
version_iii = 0 ### Fix and Small Additions

class main_engine:
    def __init__(self, genre = kl.genre[0], setting = kl.dungeon_list[0], theme = kl.theme[0], gender = kl.gender[0], creature = kl.creature_list[9],
    difficulty = 4, card = 8):
        self.genre = genre
        self.setting = setting
        self.theme = theme
        self.gender = gender
        self.creature = creature
        self.memory = []
        self.difficulty = difficulty
        for i in range(1,card):
            self.memory.append([])
    def memory_install(self, installation, card):
        self.memory[card].append(installation)
    def memory_clean(self, card):
        self.memory[card].clear()
    def memory_display(self):
        for i in range(0,len(self.memory)-1):
            print(self.memory[i], "\n")
    def get_list(self):
        return [self.genre, self.setting, self.theme, self.gender, self.creature, self.memory, self.difficulty] ### Memory then Difficulty should be last
    def remove_duplicates(self, lista):
        lista2 = []
        for item in lista:
            if item not in lista2: #is item in lista2 already?
                lista2.append(item)
            return lista2
    def fight_checker(self, card_i = 0):
        x = round(abs(mt.sin(ring())/(1**self.difficulty)), 2)
        if debug == 1:
            print("Roll:", x)
        if x < 0.10:
            print("You absolutley lose with the following;")
            rng_1 = active_kink()
            for a in range(1,rd.randint(2,3)):
                generate(lista = rng_1, engine = Engine, card = card_i)
            self.difficulty += 1
        elif x < 0.33:
            print("You may lose due to the following;")
            rng_1 = active_kink()
            for a in range(1,rd.randint(2,3)):
                generate(lista = rng_1, engine = Engine, card = card_i)
            self.difficulty += 1
        elif x < 0.50:
            print("You can easily beat the following;")
            rng_1 = active_kink()
            for a in range(1,rd.randint(2,3)):
                generate(lista = rng_1, engine = Engine, card = card_i)
            self.difficulty += 1
        else:
            print("They do not have anything to combat you with.")
            self.difficulty += 1
    def change_genre(self, new): ### New to List 1
        self.genre = new
    def change_setting(self, new):
        self.setting = new
    def change_theme(self, new):
        self.theme = new
    def change_gender(self, new):
        self.gender = new
    def change_creature(self, new):
        self.creature = new
    def change_memory(self, new):
        self.memory = new
    def change_difficulty(self, new):
        self.difficulty = new
    def c_genre(self, new):
        self.genre = new
    def c_setting(self, new):
        self.setting = new
    def c_theme(self, new):
        self.theme = new
    def c_gender(self, new):
        self.gender = new
    def c_creature(self, new):
        self.creature = new
    def c_memory(self, new):
        self.memory = new
    def c_difficulty(self, new):
        self.difficulty = new

Engine = main_engine() ### <===== Engine to mod for campaigns you horny fuck 8

def fill_traits(Engine = Engine):
    Get = Engine.get_list()
    for i in range(0,len(Get)-2):
        kl.Traits.append(Get[i])

'''
Engine Notes
Genre is the style of the story.
Setting is the location.
Theme is the story plot.
Gender is the character's biological gender.
Cards is lists that story memories from RSGs.
Difficulty is how hard it is for the character to escape.
'''
def ring():
    return rd.randint(1,360)

def active_kink():
    x = ring()
    if x >= 1 and x < 217:
        return kl.kink_list_of_lists[0]
    elif x >= 200 and x < 260:
        return kl.kink_list_of_lists[1]
    elif x >= 260 and x < 330:
        return kl.kink_list_of_lists[6]
    elif x >= 330 and x < 361:
        return kl.kink_list_of_lists[9]
    else:
        print("Error, check numbers.")

def duplication_check(engine, dice, card):
    a = engine.memory[card].count(dice)
    x = rd.randint(1,20)
    num_i = ((x**2))/(1+a)
    if dice in engine.memory[card] and num_i < 4:
        return True
    else:
        return False

def factorate(engine = Engine, lister = [], dice = 0, card_num = 0):
    result = False
    step = 0
    memory_list = engine.get_list()[4]
    dupe_disallowed = duplication_check(Engine, dice, card_num)
    while step == 0:
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        if dupe_disallowed == True:
            return result
        else:
            step = step + 1

    while step == 1:
        if step in cf.SKIP_STEPS:
            step = step + 1
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        if 0 not in lister[dice][1]:
            for i in range(0, len(lister[dice][1])):
                if lister[dice][1][i][0] in engine.gender[0]:
                    step = step + 1
            if step != 2:
                return result
        else:
            step = step + 1

    while step == 2:
        if step in cf.SKIP_STEPS:
            step = step + 1
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        if 0 not in lister[dice][2]:
            popular_check = (rd.randint(1,300))/100
            for i in range(0, len(lister[dice][2][0])):
                if lister[dice][2][0][i] in engine.genre[0] and popular_check <= lister[dice][2][1]:
                    step = step + 1
            if step != 3:
                return result
        else:
            step = step + 1

    while step == 3:
        if step in cf.SKIP_STEPS:
            step = step + 1
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        if 0 not in lister[dice][3]:
            num_i = rd.randint(0,100)
            for i in range(0, len(lister[dice][3])):
                if lister[dice][3][0][i] in engine.theme[0] and num_i < lister[dice][3][3][i]:
                    step = step + 1
            if step != 4:
                return result
        else:
            step = step + 1

    while step == 4:
        if step in cf.SKIP_STEPS:
            step = step + 1
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        if lister[dice] in engine.memory[card_num]:
            x = r(1,100)
            if engine.memory[card_num].count(lister[dice]) <= 0:
                result = x/engine.memory[card_num].count(lister[dice])
            else:
                result = 1
            if result < 50:
                step = step + 1
            else:
                return result
        else:
            step = step + 1
        
    while step == 5: ### <====== Final step, increase when you add more factors you kinky fish frog
        if debug == 1:
            print(step)
            ti.sleep(cf.TIME_DELAYS)
        engine.memory_install(lister[dice], card_num)
        kl.Traits.append(lister[dice])
        result = True
        return result

def random_theme():
        quant_list = []
        for i in range(0,len(kl.theme)):
            for x in range(0,len(kl.theme[i])):
                    quant_list.append(kl.theme[x])
        y = rd.randint(0,len(quant_list)-1)
        return quant_list[y]

def r(x,y):
        print(rd.randint(x,y))

def limbs(arms = 2, legs = 2, restrictions = -1):
    ### 0: "Left Side", 1: "Right Side", 2: "Front Side", 3: "Back Side"
    arms_result = rd.randint(1,arms)
    legs_result = rd.randint(1,legs)
    if restrictions == 0:
        AL_rng = rd.randint(1,2)
        if (arms_result < mt.ceil(arms/2) and legs_result > mt.floor(legs/2)) or (AL_rng == 1 and legs_result > mt.floor(legs/2)):
            print(arms_result, "arm")
        elif (arms_result > mt.ceil(arms/2) and legs_result < mt.floor(legs/2)) or (AL_rng == 2 and arms_result > mt.ceil(arms/2)):
            print(arms_result, "leg")
    elif restrictions == 1:
        AL_rng = rd.randint(1,2)
        if (arms_result > mt.ceil(arms/2) and legs_result < mt.floor(legs/2)) or (AL_rng == 1 and legs_result < mt.floor(legs/2)):
            print(arms_result, "arm")
        elif (arms_result < mt.ceil(arms/2) and legs_result > mt.floor(legs/2)) or (AL_rng == 2 and arms_result < mt.ceil(arms/2)):
            print(arms_result, "leg")
        elif restrictions == 2:
            print(arms_result, "arm")
        elif restrictions == 3:
            print(arms_result, "leg")
    else:
        AL_rng = rd.randint(1,2)
        if AL_rng == 1:
            print(arms_result, "arm")
        elif AL_rng == 2:
            print(arms_result, "leg")

def generate(lista = kl.action_list, engine = Engine, card = -1):
    while True:
        x = rd.randint(0,len(lista)-1)
        if debug == 1:
            print("Roll: ", x)
            print("End:", len(lista))
            ti.sleep(cf.TIME_DELAYS)
        if factorate(lister = lista, dice = x) is True:
            result = lista[x][0][0]
            print(result)
            if card > 0 and card <= len(engine.memory):
                engine.memory_install[card].append(result)
            break        

def all():
    cal = rd.randint(1,len(kl.kink_list_of_lists)-1)
    result = kl.kink_list_of_lists[cal]
    return result

def g(lista = kl.action_list, engine = Engine, card = -1):
    while True:
        x = rd.randint(0,len(lista)-1)
        if debug == 1:
            print("Roll: ", x)
            print("End:", len(lista))
            ti.sleep(cf.TIME_DELAYS)
        if factorate(lister = lista, dice = x) is True:
            result = lista[x][0][0]
            print(result)
            if card > 0 and card <= len(engine.memory):
                engine.memory_install[card].append(result)
            break

def bring():
    x = rd.randint(0,len(kl.kink_list_of_lists))
    y = rd.randint(0,len(kl.kink_list_of_lists[x]))

def quicky(debug = 0):
    ring = rd.randint(1,360)
    tier = int(round(abs(rd.randint(1,7)*mt.cos(ring)), 0))
    if tier == 1:
        x = rd.randint(0,11)
        print(kl.quick_list_s[x])
    elif tier == 2:
        x = rd.randint(0,15)
        print(kl.quick_list_a[x])
    elif tier == 3:
        x = rd.randint(0,8)
        print(kl.quick_list_b[x])
    elif tier == 4:
        x = rd.randint(0,12)
        print(kl.quick_list_c[x])
    elif tier == 5:
        x = rd.randint(0,1)
        print(kl.quick_list_d[x])
    elif tier == 6:
        x = rd.randint(0,4)
        print(kl.quick_list_e[x])
    elif tier == 7:
        x = rd.randint(0,5)
        print(kl.quick_list_f[x])
    else:
        x = rd.randint(0,11)
        print(kl.quick_list_s[x])
    if debug == 1:
        print(tier)
        

def danger_escape_allow(num = danger_encounters):
    danger_encounters =+ 1
    ring = rd.randint(1,360)
    x = round(abs(mt.sin(ring)*(2**danger_encounters)), 2)
    if x < 0.33:
        print("You can't escape")
        danger_encounters += 1
        return danger_encounters
    else:
        print("You can escape.")
        danger_encounters += 1
        return danger_encounters

def dea(num = danger_encounters):
    danger_encounters =+ 1
    ring = rd.randint(1,360)
    x = abs(mt.sin(ring)*(2**danger_encounters))
    if x < 0.33:
        print("You can't escape")
        danger_encounters += 1
        return danger_encounters
    else:
        print("You can escape.")
        danger_encounters += 1
        return danger_encounters

def test_range_dea():
    danger_escape_allow()
    danger_escape_allow()
    danger_escape_allow()
    danger_escape_allow()
    danger_escape_allow()
    danger_encounters = 0

if debug == 1:
    g(card = 0)

fill_traits()

print("AIDS v"+str(version_i)+"."+str(version_ii)+"."+str(version_iii))

