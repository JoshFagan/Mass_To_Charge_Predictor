import argparse 


def parse_arguments():
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

    parser.add_argument( '-c', '--charge', 
                         type=int, nargs=1, required=True,
                         help='Charge of experiment.' )

    args = parser.parse_args()

    # Check to ensure if a list of building blocks is supplied than a list 
    # of quantities is supplied as well, and vise versa
    if ((args.building_blocks and not args.quantities) or  
        (not args.building_blocks and args.quantities)):
        parser.error('The following arguments are mutually inclusive: \
                      building_blocks, quantities')


def main():
    parse_arguments()


if __name__ == "__main__":
    main()
