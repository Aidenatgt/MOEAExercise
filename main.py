import random
import matplotlib.pyplot as plt

trials: list[tuple[int, int, int, int, int]] = []

def domination_table(trials: list[tuple[int, int, int, int, int]]) -> list[list[int]]:

def main():
    for i in range(10):
        trials.append(
            (
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            )
        )
    for trial in range(len(trials)):
        print(f"Trial: {trial} - {trials[trial]}")


if __name__ == "__main__":
    main()
