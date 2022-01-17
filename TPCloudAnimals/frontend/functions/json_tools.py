import json
import os

path = "frontend/static/js/config.json"
        
def save_config(listeAnimals, favorite):
    try:
        dict = json.loads(listeAnimals)
        dict2 = json.loads(favorite)

        finalDict = {'possibleAnimals':dict}
        finalDict['favoriteAnimal'] = dict2

        os.path.isfile(path)
        with open(path, 'w') as f:
            json.dump(finalDict, f)
    except OSError:
        print('cannot open',path)
    