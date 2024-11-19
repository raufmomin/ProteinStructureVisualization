def split_pdb_by_model(input_pdb_path):
    with open(input_pdb_path, 'r') as infile:
        pdb_content = infile.readlines()

    models = []
    current_model = []

    for line in pdb_content:
        if line.startswith('MODEL'):
            if current_model:
                models.append(current_model)
            current_model = [line]
        else:
            current_model.append(line)

    if current_model:
        models.append(current_model)

    for i, model in enumerate(models, start=1):
        output_pdb_path = f'model_{i}.pdb'
        with open(output_pdb_path, 'w') as outfile:
            outfile.writelines(model)

        print(f'Model {i} saved to {output_pdb_path}')

input_pdb_path = 'PED00020e001_data/ensemble/PED00020e001.pdb'
split_pdb_by_model(input_pdb_path)