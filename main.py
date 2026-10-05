import random
import matplotlib.pyplot as plt

from mouse_fitness import MouseFitness

trials: list[MouseFitness] = []


def domination_table(trials: list[MouseFitness]) -> list[list[int]]:
    pass


def main():
    for i in range(10):
        trials.append(
            MouseFitness(
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            )
        )
    print("Trial\tPrice\tCord Length\tDPI\tErgonomics\tClick Quality")
    for trial in range(len(trials)):
        print(f"{trial}\t{trials[trial].row_str()}")


if __name__ == "__main__":
    main()
