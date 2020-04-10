import pandas as pd
import re

import math

def get_block_masses( blocks ):
    block_masses = {}

    atomic_masses = pd.read_csv( './Data/Periodic_Table_of_Elements.csv' )
    mass_dict = atomic_masses.set_index('Symbol').to_dict()['AtomicMass']

    for block in blocks:
        block_masses[block] = 0

        molecules = re.findall( '[A-Z][^A-Z]*', block ) 
        for molecule in molecules:
            parsed_molecule = re.findall(r'(\w+?)(\d+)', molecule)
            if not parsed_molecule:
                parsed_molecule = [(molecule, 1)]

            atom   = parsed_molecule[0][0]
            weight = int(parsed_molecule[0][1])
            atomic_mass = mass_dict[atom]
            weighted_atomic_mass = atomic_mass * weight

            block_masses[block] += weighted_atomic_mass

    return block_masses
