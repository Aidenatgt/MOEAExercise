import random
import matplotlib.pyplot as plt

from mouse_fitness import MouseFitness, MultiObjectiveMouseFitness
from digraph import Digraph

trials: list[MultiObjectiveMouseFitness] = []


def construct_digraph(trials: list[MultiObjectiveMouseFitness]) -> Digraph:
    graph = Digraph([f"Trial {i}" for i in range(len(trials))])

    for trial_num in range(len(trials)):
        for other_trial_num in range(len(trials)):
            if trial_num != other_trial_num:
                if trials[trial_num].dominates(trials[other_trial_num]):
                    graph.add_edge(f"Trial {trial_num}", f"Trial {other_trial_num}")

    return graph


def domination_table(trials: list[MultiObjectiveMouseFitness]) -> list[list[int]]:
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
            MultiObjectiveMouseFitness([random.randint(1, 10) for _ in range(2)])
        )

    for _ in range(4):
        for trial_num, trial in enumerate(trials):
            print(f"Trial {trial_num}: {trial}")
        domination_results = domination_table(trials)
        for trial_num, dominated_trials in enumerate(domination_results):
            print(f"Trial {trial_num} dominates trials: {dominated_trials}")
        print("\n")

        construct_digraph(trials).render()
        for trial in trials:
            trial.qualities.append(random.randint(1, 10))


if __name__ == "__main__":
    main()
