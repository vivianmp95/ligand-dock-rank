# LigandDockRank

LigandDockRank is a script developed in Python with the aim of selecting the best molecular docking models based on the shortest distances between the ligand and the active site. After running the script, you will find a file in .csv format containing the information that will allow you to select the best docking model.

### 📋 Prerequisites

To run the script, you need to have Python3 installed.

### 📁 Subfolders

**Ligands**: This directory should contain only the docking files. Examples have been provided to demonstrate the expected file format.

**Receptor**: This directory should contain the receptor file named "receptor.pdb." For reference, an example receptor file, "Crystal structure of HIV-1 reverse transcriptase in complex with S-1153" (PDB ID: 7MEQ; REN et al., 2000), is included in the "receptor" folder.

Obs: The provided "ligands" folder includes docking poses of a hydrolase activator (PDB ID: 2HI8; ROESER et al., 2007) in complex with the receptor. This serves as an illustrative example to help you understand the expected input and output of the script.

### 🔧 Running

1. Open the receptor's .pdb file and locate the active site line.
2. Replace the content of line 46 in the script with the first three columns of the identified active site line.

```
if 'ATOM   5086  N' in line:
```

2. On line 14, you must enter the type of your active site residue, among the options: Hydrophobic, Aromatic, Positive, Negative, Donor or Acceptor.

```
receptor_type = 'Acceptor'
```

To run the script for the first time, you must first install its dependencies. To do so, you should run the following command on the root folder:

```
pip install
```

With the dependencies installed, run the script with the following command:

```
python3 script.py
```

When finished running, you will find in your folder a file with the name "output.csv" containing information about the atom, the corresponding docking model, the distance from the atom to the active site, an indication whether it is a good inhibitor or not (considering a maximum distance of 6A) and the binding type.

## 📄 License

This project is under the MIT License - see the [LICENSE.md](https://github.com/vivianmp95/ligand-dock-rank/blob/main/LICENSE) file for details.

---
Made with ❤️ by [Vivian Paixão](https://github.com/vivianmp95) 😊
