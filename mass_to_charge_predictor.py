from get_specifications import get_experiment_specs 


def main():
    """Collect inputs about experiemnt from user and return building block
       combinations that result in the desired mass."""

    specs = get_experiment_specs()

    print( specs )


if __name__ == "__main__":
    main()
