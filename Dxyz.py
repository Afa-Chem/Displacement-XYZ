#!/usr/bin/env python

import numpy as np

def read_xyz_file(file_path):
    """
    Read atomic coordinates from an XYZ file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_atoms = int(lines[0])
            atomic_coordinates = []
            for line in lines[2:]:
                parts = line.split()
                atomic_coordinates.append((parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
            return atomic_coordinates
    except FileNotFoundError:
        print("File not found or path is incorrect:", file_path)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    

def calculate_displacement(atom_coords1, atom_coords2):
    """
    Calculate the displacement between two sets of atomic coordinates.
    """
    if len(atom_coords1) != len(atom_coords2):
        print("Error: Number of atoms does not match between the two structures.")
        return None
    
    atomic_displacement = []
    atoms = []
    for i in range(len(atom_coords1)):
        atom1 = atom_coords1[i]
        atom2 = atom_coords2[i]
        atomic_displacement.append(float(np.sqrt(((atom2[1] - atom1[1])**2 + (atom2[2] - atom1[2])**2 + (atom2[3] - atom1[3])**2))))    
        atoms.append(atom1[0])
    
    displacement = [[atoms[i], atomic_displacement[i]] for i in range(min(len(atoms), len(atomic_displacement)))]
    
    return displacement



def mean_displacement(displacement):
    """
    Calculate the mean atomic displacement
    """
    if len(displacement) == 0:
        print("Error: The displacement set is empty")
        return None
    
    dx = []
    for i in displacement: 
        dx.append(i[1])
    
    mean=np.mean(dx)
    
    return mean


# File paths
file_path_initial = input("Enter the path to the initial XYZ file: ")
file_path_final = input("Enter the path to the final XYZ file: ")

# Read atomic coordinates from both files
atomic_coords1 = read_xyz_file(file_path_initial)
atomic_coords2 = read_xyz_file(file_path_final)

displacement = calculate_displacement(atomic_coords1, atomic_coords2)
mean = mean_displacement(displacement)

if atomic_coords1 is not None and atomic_coords2 is not None:
    # Calculate displacement
    if displacement is not None:
        # Write displacement to a file
        output_file_path = input("Enter the name to the output file: ")
        with open(output_file_path, 'w') as output_file:
            output_file.write("Mean displacement\n")
            output_file.write(f"{str(mean)}\n")
            output_file.write("\n")
            output_file.write("Atomic displacement \n")
            output_file.write("\n")
            for atom in displacement:
                output_file.write(f"{atom[0]} {atom[1]}\n")



