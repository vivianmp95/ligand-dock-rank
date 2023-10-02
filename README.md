# LigandDockRank

LigandDockRank is a script developed in Python with the aim of selecting the best molecular docking models based on the shortest distances between the ligand and the active site. After running the script, you will find a file in .csv format containing the information that will allow you to select the best docking model.

### 📋 Prerequisites

To run the script, you need to have Python3 installed.

### 📁 Subfolders

**Ligands**: directory that will receive the docking files (ATTENTION: the folder must only contain the docking files).
**Receiver**: directory that will receive the receiver file, with the name "receiver.pdb".

### 🔧 Running

1. To configure your target, you must open the receiver's .pdb file and find the active site line. When found, replace in line 55 with the first three columns of that line.

```
if 'ATOM   2097  OG' in line:
```

2. On line 23, you must enter the type of your active site residue, among the options: Hydrophobic, Aromatic, Positive, Negative, Donor or Acceptor.

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