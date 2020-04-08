from parse_specifications import get_specs
from parse_building_blocks import get_block_masses 


def main():
    """Collect inputs about experiemnt from user and return building block
       combinations that result in the desired mass."""

    specs = get_specs()
    print( specs )

    block_masses = get_block_masses( specs.building_blocks )
    print( block_masses )


if __name__ == "__main__":
    main()
