import os
import csv

from scipy.spatial import distance

path = os.getcwd()  # Obtains your current working directory
path_list = []
valid_extensions = [".pdb"]  # specify your valid extensions here
final_list = []
receptor_coordinates = []
distance_list = []
model_data = {}
header_name = ''
receptor_type = 'Acceptor'

# CONTATOS (baseado na definição do nAPOLI)
# tipo = (distancia_minima, distancia_maxima)
contacts = {'ALA:N': [0, 0, 0, 0, 1, 0], 'ALA:CA': [0, 0, 0, 0, 0, 0], 'ALA:C': [0, 0, 0, 0, 0, 0], 'ALA:O': [0, 0, 0, 0, 0, 1], 'ALA:CB': [1, 0, 0, 0, 0, 0], 'ARG:N': [0, 0, 0, 0, 1, 0], 'ARG:CA': [0, 0, 0, 0, 0, 0], 'ARG:C': [0, 0, 0, 0, 0, 0], 'ARG:O': [0, 0, 0, 0, 0, 1], 'ARG:CB': [1, 0, 0, 0, 0, 0], 'ARG:CG': [1, 0, 0, 0, 0, 0], 'ARG:CD': [0, 0, 0, 0, 0, 0], 'ARG:NE': [0, 0, 1, 0, 1, 0], 'ARG:CZ': [0, 0, 1, 0, 0, 0], 'ARG:NH1': [0, 0, 1, 0, 1, 0], 'ARG:NH2': [0, 0, 1, 0, 1, 0], 'ASN:N': [0, 0, 0, 0, 1, 0], 'ASN:CA': [0, 0, 0, 0, 0, 0], 'ASN:C': [0, 0, 0, 0, 0, 0], 'ASN:O': [0, 0, 0, 0, 0, 1], 'ASN:CB': [1, 0, 0, 0, 0, 0], 'ASN:CG': [0, 0, 0, 0, 0, 0], 'ASN:OD1': [0, 0, 0, 0, 0, 1], 'ASN:ND2': [0, 0, 0, 0, 1, 0], 'ASP:N': [0, 0, 0, 0, 1, 0], 'ASP:CA': [0, 0, 0, 0, 0, 0], 'ASP:C': [0, 0, 0, 0, 0, 0], 'ASP:O': [0, 0, 0, 0, 0, 1], 'ASP:CB': [1, 0, 0, 0, 0, 0], 'ASP:CG': [0, 0, 0, 0, 0, 0], 'ASP:OD1': [0, 0, 0, 1, 0, 1], 'ASP:OD2': [0, 0, 0, 1, 0, 1], 'CYS:N': [0, 0, 0, 0, 1, 0], 'CYS:CA': [0, 0, 0, 0, 0, 0], 'CYS:C': [0, 0, 0, 0, 0, 0], 'CYS:O': [0, 0, 0, 0, 0, 1], 'CYS:CB': [1, 0, 0, 0, 0, 0], 'CYS:SG': [0, 0, 0, 0, 1, 1], 'GLN:N': [0, 0, 0, 0, 1, 0], 'GLN:CA': [0, 0, 0, 0, 0, 0], 'GLN:C': [0, 0, 0, 0, 0, 0], 'GLN:O': [0, 0, 0, 0, 0, 1], 'GLN:CB': [1, 0, 0, 0, 0, 0], 'GLN:CG': [1, 0, 0, 0, 0, 0], 'GLN:CD': [0, 0, 0, 0, 0, 0], 'GLN:OE1': [0, 0, 0, 0, 0, 1], 'GLN:NE2': [0, 0, 0, 0, 1, 0], 'GLU:N': [0, 0, 0, 0, 1, 0], 'GLU:CA': [0, 0, 0, 0, 0, 0], 'GLU:C': [0, 0, 0, 0, 0, 0], 'GLU:O': [0, 0, 0, 0, 0, 1], 'GLU:CB': [1, 0, 0, 0, 0, 0], 'GLU:CG': [1, 0, 0, 0, 0, 0], 'GLU:CD': [0, 0, 0, 0, 0, 0], 'GLU:OE1': [0, 0, 0, 1, 0, 1], 'GLU:OE2': [0, 0, 0, 1, 0, 1], 'GLY:N': [0, 0, 0, 0, 1, 0], 'GLY:CA': [0, 0, 0, 0, 0, 0], 'GLY:C': [0, 0, 0, 0, 0, 0], 'GLY:O': [0, 0, 0, 0, 0, 1], 'HIS:N': [0, 0, 0, 0, 1, 0], 'HIS:CA': [0, 0, 0, 0, 0, 0], 'HIS:C': [0, 0, 0, 0, 0, 0], 'HIS:O': [0, 0, 0, 0, 0, 1], 'HIS:CB': [1, 0, 0, 0, 0, 0], 'HIS:CG': [0, 1, 0, 0, 0, 0], 'HIS:ND1': [0, 1, 1, 0, 1, 1], 'HIS:CD2': [0, 1, 0, 0, 0, 0], 'HIS:CE1': [0, 1, 0, 0, 0, 0], 'HIS:NE2': [0, 1, 1, 0, 1, 1], 'ILE:N': [0, 0, 0, 0, 1, 0], 'ILE:CA': [0, 0, 0, 0, 0, 0], 'ILE:C': [0, 0, 0, 0, 0, 0], 'ILE:O': [0, 0, 0, 0, 0, 1], 'ILE:CB': [1, 0, 0, 0, 0, 0], 'ILE:CG1': [1, 0, 0, 0, 0, 0], 'ILE:CG2': [1, 0, 0, 0, 0, 0], 'ILE:CD1': [1, 0, 0, 0, 0, 0], 'LEU:N': [0, 0, 0, 0, 1, 0], 'LEU:CA': [0, 0, 0, 0, 0, 0], 'LEU:C': [0, 0, 0, 0, 0, 0], 'LEU:O': [0, 0, 0, 0, 0, 1], 'LEU:CB': [1, 0, 0, 0, 0, 0], 'LEU:CG': [1, 0, 0, 0, 0, 0], 'LEU:CD1': [1, 0, 0, 0, 0, 0], 'LEU:CD2': [1, 0, 0, 0, 0, 0], 'LYS:N': [0, 0, 0, 0, 1, 0], 'LYS:CA': [0, 0, 0, 0, 0, 0], 'LYS:C': [0, 0, 0, 0, 0, 0], 'LYS:O': [0, 0, 0, 0, 0, 1], 'LYS:CB': [1, 0, 0, 0, 0, 0], 'LYS:CG': [1, 0, 0, 0, 0, 0], 'LYS:CD': [1, 0, 0, 0, 0, 0], 'LYS:CE': [0, 0, 0, 0, 0, 0], 'LYS:NZ': [0, 0, 1, 0, 1, 0], 'MET:N': [0, 0, 0, 0, 1, 0], 'MET:CA': [0, 0, 0, 0, 0, 0], 'MET:C': [0, 0, 0, 0, 0, 0], 'MET:O': [0, 0, 0, 0, 0, 1], 'MET:CB': [1, 0, 0, 0, 0, 0], 'MET:CG': [1, 0, 0, 0, 0, 0], 'MET:SD': [0, 0, 0, 0, 0, 1], 'MET:CE': [1, 0, 0, 0, 0, 0], 'PHE:N': [0, 0, 0, 0, 1, 0], 'PHE:CA': [0, 0, 0, 0, 0, 0], 'PHE:C': [0, 0, 0, 0, 0, 0], 'PHE:O': [0, 0, 0, 0, 0, 1], 'PHE:CB': [1, 0, 0, 0, 0, 0], 'PHE:CG': [1, 1, 0, 0, 0, 0], 'PHE:CD1': [1, 1, 0, 0, 0, 0], 'PHE:CD2': [1, 1, 0, 0, 0, 0], 'PHE:CE1': [1, 1, 0, 0, 0, 0], 'PHE:CE2': [1, 1, 0, 0, 0, 0], 'PHE:CZ': [1, 1, 0, 0, 0, 0], 'PRO:N': [0, 0, 0, 0, 0, 0], 'PRO:CA': [0, 0, 0, 0, 0, 0], 'PRO:C': [0, 0, 0, 0, 0, 0], 'PRO:O': [0, 0, 0, 0, 0, 1], 'PRO:CB': [1, 0, 0, 0, 0, 0], 'PRO:CG': [1, 0, 0, 0, 0, 0], 'PRO:CD': [0, 0, 0, 0, 0, 0], 'SER:N': [0, 0, 0, 0, 1, 0], 'SER:CA': [0, 0, 0, 0, 0, 0], 'SER:C': [0, 0, 0, 0, 0, 0], 'SER:O': [0, 0, 0, 0, 0, 1], 'SER:CB': [0, 0, 0, 0, 0, 0], 'SER:OG': [0, 0, 0, 0, 1, 1], 'THR:N': [0, 0, 0, 0, 1, 0], 'THR:CA': [0, 0, 0, 0, 0, 0], 'THR:C': [0, 0, 0, 0, 0, 0], 'THR:O': [0, 0, 0, 0, 0, 1], 'THR:CB': [0, 0, 0, 0, 0, 0], 'THR:OG1': [0, 0, 0, 0, 1, 1], 'THR:CG2': [1, 0, 0, 0, 0, 0], 'TRP:N': [0, 0, 0, 0, 1, 0], 'TRP:CA': [0, 0, 0, 0, 0, 0], 'TRP:C': [0, 0, 0, 0, 0, 0], 'TRP:O': [0, 0, 0, 0, 0, 1], 'TRP:CB': [1, 0, 0, 0, 0, 0], 'TRP:CG': [1, 1, 0, 0, 0, 0], 'TRP:CD1': [0, 1, 0, 0, 0, 0], 'TRP:CD2': [1, 1, 0, 0, 0, 0], 'TRP:NE1': [0, 1, 0, 0, 1, 0], 'TRP:CE2': [0, 1, 0, 0, 0, 0], 'TRP:CE3': [1, 1, 0, 0, 0, 0], 'TRP:CZ2': [1, 1, 0, 0, 0, 0], 'TRP:CZ3': [1, 1, 0, 0, 0, 0], 'TRP:CH2': [1, 1, 0, 0, 0, 0], 'TYR:N': [0, 0, 0, 0, 1, 0], 'TYR:CA': [0, 0, 0, 0, 0, 0], 'TYR:C': [0, 0, 0, 0, 0, 0], 'TYR:O': [0, 0, 0, 0, 0, 1], 'TYR:CB': [1, 0, 0, 0, 0, 0], 'TYR:CG': [1, 1, 0, 0, 0, 0], 'TYR:CD1': [1, 1, 0, 0, 0, 0], 'TYR:CD2': [1, 1, 0, 0, 0, 0], 'TYR:CE1': [1, 1, 0, 0, 0, 0], 'TYR:CE2': [1, 1, 0, 0, 0, 0], 'TYR:CZ': [0, 1, 0, 0, 0, 0], 'TYR:OH': [0, 0, 0, 0, 1, 1], 'VAL:N': [0, 0, 0, 0, 1, 0], 'VAL:CA': [0, 0, 0, 0, 0, 0], 'VAL:C': [0, 0, 0, 0, 0, 0], 'VAL:O': [0, 0, 0, 0, 0, 1], 'VAL:CB': [1, 0, 0, 0, 0, 0], 'VAL:CG1': [1, 0, 0, 0, 0, 0], 'VAL:CG2': [1, 0, 0, 0, 0, 0]}
ligand_types = {}
for atom in contacts:
    atom_data = []
    if contacts[atom][0] == 1:
        atom_data.append("Hydrophobic")
    if contacts[atom][1] == 1:
        atom_data.append("Aromatic")
    if contacts[atom][2] == 1:
        atom_data.append("Positive")
    if contacts[atom][3] == 1:
        atom_data.append("Negative")
    if contacts[atom][4] == 1:
        atom_data.append("Donor")
    if contacts[atom][5] == 1:
        atom_data.append("Acceptor")
    if atom_data:
        ligand_types[atom] = atom_data

aromatic_range = (2, 4)
hydrogen_bond_range = (2.8, 3.9)
hydrophobic_range = (2, 4.5)
repulsive_range = (2, 6)
attractive_range = (2, 6)

# Abrir arquivo do receptor:
receptor_file = open("receptor/receptor.pdb", "r")
for line in receptor_file.readlines():
    if 'ATOM   2097  OG' in line:
        coordinates = line[32:54]
        receptor_coordinates = coordinates.split()  # criar uma lista de coordenadas da Ser441

# Abrir os arquivos de ligantes:
for file in sorted(os.listdir(path + '/ligands')):  # vai pegar os arquivos da pasta de ligantes
    extension = os.path.splitext(file)[1]
    if extension.lower() in valid_extensions:
        path_list.append(os.path.join(path + '/ligands', file))

for pdb_file in path_list:  # para cada arquivo pdb na pasta de ligantes
    current_file = open(pdb_file, "r")  # vai abrir o arquivo
    file_data = current_file.readlines()[:-2]  # do arquivo, vai tirar as linhas que não são átomos
    file_data = list(filter(lambda a: a != 'TER\n', file_data))  # vai tirar as linhas TER ao longo do arquivo
    file_type = 'protein'
    if file_data[3].split()[-1] == 'peptide_models.pdb' or file_data[2].split()[-1] == 'peptide_1.pdb':  # arquivos que têm apenas o ligante
        remark_score = file_data[3].split()[-1]
        file_type = 'peptide'
    else:  # arquivos que têm o ligante e o receptor
        remark_score = file_data[3].split()[2]
    escrever = False

    for line in file_data:  # para cada linha no arquivo
        local_model = model_data.copy()

        if 'MODEL' in line:  # deixar apenas os ligantes (filtrar linhas anteriores a header) e tirar o receptor
            header_name = line.split()[1]

        if file_type == 'peptide' or file_type == 'protein' and 'HEADER' in line:
            escrever = True

        if escrever == True and 'ATOM' in line:  # tratamento dos dados, pega apenas os ATOM
            if (line[13] == 'C' and line[14] in [' ', 'A']) or (
                    (line[13] == 'N' or line[13] == 'O') and line[14] == ' '):
                aminoacid = ":".join(line[:-3].split()[2:4][::-1])
                coordinates = line[:-2].split()[-3:]

                local_model.update({'aminoacid': aminoacid})
                local_model.update({'ligand': header_name})
                local_model.update({'remark_score': remark_score})
                local_model.update({'coordinates': coordinates})
                final_list.append(local_model.copy())

for item in final_list:  # cálculo da distância euclidiana
    result_data = model_data.copy()
    item_data = item.copy()
    formatted_recept = list(map(float, receptor_coordinates))
    formatted_item = list(map(float, item_data['coordinates']))
    distance_value = distance.euclidean(formatted_recept, formatted_item)

    result_data.update({'aminoacid': item_data['aminoacid']})
    result_data.update({'ligand': item_data['ligand']})
    result_data.update({'remark_score': item_data['remark_score']})
    result_data.update({'coordinates': item_data['coordinates']})
    result_data.update({'distance': distance_value})

    if distance_value <= 6:  # vai filtrar pelos aminoácidos com distância euclidiana menor que 5A
        result_data.update({'Is it a good candidate?': 'true'})
    else:
        result_data.update({'Is it a good candidate?': 'false'})

    if item_data['aminoacid'] in ligand_types.keys():
        current_ligand_types = ligand_types[item_data['aminoacid']]
        for ltype in current_ligand_types:
            if ltype == 'Donor' and receptor_type == 'Acceptor' and (min(hydrogen_bond_range[0], hydrogen_bond_range[1]) < distance_value < max(hydrogen_bond_range[0], hydrogen_bond_range[1])):
                result_data.update({'bond_type': 'Hydrogen Bond'})
            elif ltype == 'Aromatic' and receptor_type == 'Aromatic' and (min(aromatic_range[0], aromatic_range[1]) < distance_value < max(aromatic_range[0], aromatic_range[1])):
                result_data.update({'bond_type': 'Aromatic'})
            elif ltype == 'Hydrophobic' and receptor_type == 'Hydrophobic' and (min(hydrophobic_range[0], hydrophobic_range[1]) < distance_value < max(hydrophobic_range[0], hydrophobic_range[1])):
                result_data.update({'bond_type': 'Hydrophobic'})
            elif (ltype == 'Positive' and receptor_type == 'Negative') or (ltype == 'Negative' and receptor_type == 'Positive') and (min(repulsive_range[0], repulsive_range[1]) < distance_value < max(repulsive_range[0], repulsive_range[1])):
                result_data.update({'bond_type': 'Repulsive'})
            elif (ltype == 'Positive' and receptor_type == 'Positive') or (ltype == 'Negative' and receptor_type == 'Negative') and (min(attractive_range[0], attractive_range[1]) < distance_value < max(attractive_range[0], attractive_range[1])):
                result_data.update({'bond_type': 'Attractive'})
            else:
                result_data.update({'bond_type': '-'})
    else:
        result_data.update({'bond_type': '-'})

    distance_list.append(result_data.copy())
distance_list = sorted(distance_list, key=lambda d: d['distance'])
minor_distance = distance_list[0]['distance']
if minor_distance > 6:
    print('AVISO: Distâncias são maiores que 6A, não são bons candidatos. Conferir output.')

# Criação do output com os resultados
keys = distance_list[0].keys()

with open('output.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(distance_list)
