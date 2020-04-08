from parse_specifications import get_specs
from parse_building_blocks import get_block_masses 
#from sets import Set


def sum_of_blocks_masses( blocks, block_masses ):
    masses = []
    for i in range( len( blocks ) ):
        masses.append(  block_masses[blocks[i]] )

    return sum( masses ) 

def subset_sum( blocks, target_mass, block_masses, partial=[], candidates=set([]) ):
    partial_sum = sum_of_blocks_masses( partial, block_masses )

    # check if the partial sum is equals to target
    if partial_sum  == target_mass: 
        candidates.add( tuple(partial) )
    if partial_sum >= target_mass:
        return  candidates # if we reach the number why bother to continue

    for i in range( len( blocks ) ):
        block = blocks[i]
        remaining = blocks[i+1:]
        candidates.union( subset_sum( remaining, target_mass, block_masses, partial + [block], candidates ) ) 

    return candidates


def find_candidates( specs, block_masses ):
    charged_mass = specs.observed_mass * specs.charge
    blocks = []
    for i in range( len( specs.building_blocks ) ):
        for j in range( specs.quantities[i] ):
            blocks.append( specs.building_blocks[i] ) 

    return subset_sum( blocks, charged_mass, block_masses )


def main():
    """Collect inputs about experiemnt from user and return building block
       combinations that result in the desired mass."""

    specs = get_specs()

    block_masses = get_block_masses( specs.building_blocks )

    candidates = find_candidates( specs, block_masses )

    print( 'Possible candidates are:' )
    for candidate in candidates:
        print( candidate )



if __name__ == "__main__":
    main()
