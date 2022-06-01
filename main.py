from level import Level


def main():
    print("Welcome to the level calculator!\n")
    l1 = Level()
    l1.take_level_points()

    print(f"{l1.results=}")
    print(f"{l1.highest_point_level=}")
    print(f"{l1.lowest_point_level=}")
    print("\n")
    print(f"{l1.invalid_points=}")
    print(f"{l1.invalid_inputs=}")
    print("\n")
    print(f"{l1.invalid_level_points=}")

    l1.output_to_csv()



if __name__ == '__main__':
    main()
