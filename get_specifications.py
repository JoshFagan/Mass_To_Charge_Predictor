import argparse
import pandas as pd


def get_args():
    """Define arguments to be parsed from user."""

    parser = argparse.ArgumentParser( description='Select building blocks \
                                                   to fit required mass.' )
    group = parser.add_mutually_exclusive_group()

    group.add_argument( '-b', '--building_blocks', nargs='+',
                         help='List of building blocks that compose the \
                               product.' )

    parser.add_argument( '-q', '--quantities', type=int, nargs='+',
                         help='List of quantities of building blocks that \
                               compose the product.' )

    group.add_argument( '-b_file', '--building_block_file', nargs=1,
                         help='Location of file that containes building \
                               blocks and their quantities.' )

    parser.add_argument( '-c', '--charge', 
                         type=int, nargs=1, required=False,
                         help='Charge of experiment.' )

    args = parser.parse_args()

    # Check to ensure if a list of building blocks is supplied than a list 
    # of quantities is supplied as well, and vise versa.
    if ((args.building_blocks and not args.quantities) or  
        (not args.building_blocks and args.quantities)):
        parser.error('The following arguments are mutually inclusive: \
                      building_blocks, quantities')

    return args

def request_missing_specs( args ):
    # Request charge if missing
    while not args.charge:
        charge = input( 'Input interger value for charge:\n' )
        try:
            args.charge = int( charge )
        except:
            print( 'Charge must be an integer (whole number)' )

    # Request list of building blocks if missing
    if not args.building_blocks:
        blocks     = []
        quantities = []

        block = input( 'Input building block formula:\n' )
        
        # Ensure at least one building block is inputted
        while block == '':
            block = input( 'There must be at least one building block.\n' +
                           'Input building block formula:\n' )

        # Keep getting inputs until client is done
        while not block == '':
            blocks.append( block )
            block = input( 'Input additional building block formula ' +
                           '(press Enter key to finish):')

        # Get respective quantities
        for block in blocks:
            while True:
                quantity = input( 'Input quantity for ' + block + ': ' )
                try:
                    quantity = int( quantity )
                    break
                except:
                    print( 'Quantity must be a positive integer (whole number): ' )
                if quantity < 0:
                    print( 'Quantity must be a positive integer (whole number): ' )
            quantities.append( quantity )

        args.building_blocks = blocks
        args.quantities = quantities


        

    


def get_experiment_specs():
    """Retrieve experiemnt specifications from client.
    
    Specifications can come from a combination of command line arguments, 
    csv files, and standard input.
    """
    args  = get_args() 

    # If a building block file is supplied, read the file and store the 
    # building blocks and their quantities in the specs structure.
    if args.building_block_file:
        df = pd.read_csv( args.building_block_file[0], 
                          names=['blocks', 'quantities'] )

        args.building_blocks = df['blocks'].tolist()
        args.quantities      = df['quantities'].tolist()



    # Augment any missing specifications with prompts to standard input.
    request_missing_specs( args )

    return args 
