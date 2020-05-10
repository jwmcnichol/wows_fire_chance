coefficient_dic = {
    'i':[1,1],
    'ii':[1, 1],
    'iii':[1, .9667],
    'iv':[.9334, .9001],
    'v':[0.8668, 0.8335],
    'vi':[0.8002, 0.7669],
    'vii':[0.7336, 0.7003],
    'viii':[0.6670, 0.6337],
    'ix':[.6004, .5671],
    'x':[.5338, .5005]
            }

def find_fire_chance():
        tier = input('Enter target ship tier i - x ')
        is_DCM_1_present = input('Target ship has DCM1 present? Y or N')
        if is_DCM_1_present == 'Y':
            DCM1_value = .95
        else:
            DCM1_value = 1.00
        hull_value = input ('If target ship has stock hull, type Y, if not, type N.')
        rawbase_chance = float(input('Firing ship artillery base chance as a pct (7 for 7 pct)'))
        base_chance = rawbase_chance * .01
        demo_chance = float(input('Firing ship demolition expert chance - .02 is standard chance when used)'))
        victorflown = input('Firing ship Victor flag used? YN victor chance = .5%').casefold()
        if victorflown == 'Y':
            victorflown = .005
        else:
            victorflown = 0
        xray_flown = input('Firing ship Xray flag used? YN xray chance = .5%').casefold()
        if xray_flown == 'Y':
            xray_flown = .005
        else:
            xray_flown = 0
        combined_flag_chance = xray_flown + victorflown
        #print('flag chance is', combined_flag_chance)
        is_fire_prevention = input('Target ship fire prevention used?').casefold()
        if is_fire_prevention == 'y':
            fpchance = .9
        else:
            fpchance = 1.0
        IFHEused = input('Firing ship IFHE used? YN')
        if IFHEused == 'Y':
                adj_base_chance = base_chance * .5
        else:
                adj_base_chance = base_chance
        fire_resistance = 1
        #for key in coefficient_dic:
        #    stockcoefficient = 1
        #    finalhullcoefficient = 1
        #    if key == tier:
        #        coefficient_value = coefficient_dic[tier]
        #        for value in coefficient_value:
        #            stockcoefficient = coefficient_value[0]
        #            print(stockcoefficient)
        #            print(finalhullcoefficient)
        #
        #finalhullcoefficient = coefficient_value[1]
        if hull_value == 'Y':
            fire_resistance = (coefficient_dic[tier])[0]
            print(fire_resistance)
        elif hull_value == 'N':
            fire_resistance = (coefficient_dic[tier])[1]
        #print('hull value is', hull_value)
        #print(fire_resistance, 'is fire res')
        first_chunk = fire_resistance * DCM1_value
        middle_chunk = fpchance
        print(middle_chunk, 'is middle_chunk')
        print(middle_chunk, 'is fpchance')
        last_chunk = (float(adj_base_chance)) + (float(demo_chance)) + (float(combined_flag_chance))
        fire_chance = ((float(first_chunk)) * (float(middle_chunk))) * (float(last_chunk))
        print('Fire chance is', fire_chance)
find_fire_chance()

#t8 3.3 / 4.8
#t9 2.9
#yorck against 8 8.4% 12 sec reload

