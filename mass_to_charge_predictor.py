import argparse 

def main( args ):
   print( args ) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='Select building blocks \
                                                   to fit required mass.' )


    parser.add_argument( '-b', '--building_blocks', nargs='+',
                         help='List of building blocks that compose the \
                               product.' )

    parser.add_argument( '-q', '--quantities', type=int, nargs='+',
                         help='List of quantities of building blocksthat \
                               compose the product.' )

    parser.add_argument( '-b_file', '--building_block_file', nargs=1,
                         help='Location of file that containes building \
                               blocks and their quantities.' )


    parser.add_argument( '-c', '--charge', type=float, nargs=1,
                         help='Charge of experiment.' )

    args = parser.parse_args()

    main( args )

