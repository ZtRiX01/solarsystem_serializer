import yaml
import pandas as pd



def readFile(fil: str) :
    with open(fil, 'r') as file:
        sun_system_data = yaml.safe_load(file)
        return sun_system_data
    

def convert_file(sun_system_data):
    new_dict = {}

    for planet in sun_system_data['sun_system']['distance_to_sun']:
        
        p = list(planet.keys())[0]
        distance = planet[p]
        new_dict[p] = distance
        
        
    return new_dict

def calc_min_distance(new_dict):
    min ={}
    
    for planet, distance in new_dict.items():
        min[planet] = {}
        for planet2 in new_dict:
            if planet == planet2:
                min[planet][planet2] = 0
            else:
                minDis = (distance - new_dict[planet2])
                if minDis < 0:
                    min[planet][planet2] = (round(minDis, 2)) * -1
                else:
                    min[planet][planet2] = round(minDis, 2)
    return min

def calc_max_distance(new_dict):
    max ={}
    
    for planet, distance in new_dict.items():
        max[planet] = {}
        for planet2 in new_dict:
            if planet == planet2:
                max[planet][planet2] = 0
            else:
                max[planet][planet2] = round((distance + new_dict[planet2]), 2)
    print(max)
    return max

def write_to_excel(distance, filename):
    df = pd.DataFrame.from_dict(distance)

    # Excel-Datei schreiben
    df.to_excel(filename)

sun_system = readFile("solar_system.yaml")
data = convert_file(sun_system)
calc_min = calc_min_distance(data)
calc_max = calc_max_distance(data)


write_to_excel(calc_max, "max.xlsx")
write_to_excel(calc_min, "min.xlsx")