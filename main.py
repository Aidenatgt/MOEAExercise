import random
import matplotlib.pyplot as plt

from mouse_fitness import MouseFitness

trials: list[MouseFitness] = []


def domination_table(trials: list[MouseFitness]) -> list[list[int]]:
    result: list[list[int]] = [[] for _ in range(len(trials))]
    for trial_num in range(len(trials)):
        for other_trial_num in range(len(trials)):
            if trial_num != other_trial_num:
                if trials[trial_num].dominates(trials[other_trial_num]):
                    result[trial_num].append(other_trial_num)
    return result


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

    domination_results = domination_table(trials)
    for trial_num, dominated_trials in enumerate(domination_results):
        print(f"Trial {trial_num} dominates trials: {dominated_trials}")


if __name__ == "__main__":
    main()
