import json
import glob

filename = 'PED00020e005'
json_files = glob.glob(f'{filename}_data/*.json')
data = []

for file in json_files:
    with open(file, 'r') as f:
        data.extend(json.load(f))

combined_data = {
    'ensemble_id': filename,
    'conformations': []
}

model_numbers = sorted(set(conformation.get('model') for conformation in data))
print(model_numbers)

for i in model_numbers:
    conformation_entry = {
        'model': i,
    }
    for conformation_data in data:
        if conformation_data.get('model') == i:
            if conformation_data.get('dmax'):
                conformation_entry['dmax'] = conformation_data.get('dmax')
            if conformation_data.get('gyration'):
                conformation_entry['gyration'] = conformation_data.get('gyration')  
    
    combined_data['conformations'].append(conformation_entry)

with open(f'{filename}.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)
