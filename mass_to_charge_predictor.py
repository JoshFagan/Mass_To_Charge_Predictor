from parse_specifications import get_specs
from parse_building_blocks import get_block_masses 
#from sets import Set


def sum_of_blocks_masses( blocks, block_masses ):
    """Calculate the sum of masses for each block given."""
    masses = []
    for i in range( len( blocks ) ):
        masses.append(  block_masses[blocks[i]] )

    return sum( masses ) 


def subset_sum( blocks, target_mass, block_masses, thresh, partial=[], candidates=set([]) ):
    """Recursive method for solving the subset sum problem modified for this specific application.""" 
    partial_sum = sum_of_blocks_masses( partial, block_masses )

    # check if the partial sum is equals to target
    if partial_sum  >= target_mass-thresh and partial_sum <= target_mass+thresh: 
        candidates.add( tuple(partial) )
    if partial_sum >= target_mass+thresh:
        return  candidates # if we reach the number why bother to continue

    for i in range( len( blocks ) ):
        block = blocks[i]
        remaining = blocks[i+1:]
        candidates.union( subset_sum( remaining, target_mass, block_masses, thresh, partial + [block], candidates ) ) 

    return candidates


def find_candidates( specs, block_masses ):
    """Setup for finding candidates via recursive method.""" 
    charged_mass = specs.observed_mass * specs.charge
    blocks = []
    for i in range( len( specs.building_blocks ) ):
        for j in range( specs.quantities[i] ):
            blocks.append( specs.building_blocks[i] ) 

    return subset_sum( blocks, charged_mass, block_masses, specs.threshold )


def main():
    """Collect inputs about experiemnt from user and return building block
       combinations that result in the desired mass."""

    print( 'Retrieving experiment specifications from client.' )
    specs = get_specs()

    print( '\tExperiment specifications are:' )
    print( '\tCharge: %i' % specs.charge )
    print( '\tObserved Mass: %f' % specs.observed_mass )
    print( '\tThreshold: %f' % specs.threshold )
    print( '\tQuantity - Building Block:' )
    for i in range(len(specs.quantities) ):
        print( '\t\t%i - %s' % (specs.quantities[i], specs.building_blocks[i]) )


    print( '\nParsing blocks and calculating masses.' )
    block_masses = get_block_masses( specs.building_blocks )

    print( '\tBuilding Block - Mass of Building Block:' )
    for block in specs.building_blocks:
        print('\t\t%s - %f' % (block, block_masses[block] ) )


    print( '\nFinding all viable candidate block combinations.' )
    candidates = find_candidates( specs, block_masses )

    print( '\tCandidate block combinations are:', end='\n\t\t' )
    if len(candidates) == 0:
        print( 'There are no viable candidates.' )
    else:
        for candidate in candidates:
            print(  candidate, end='\n\t\t' )

    print()


if __name__ == "__main__":
    main()
