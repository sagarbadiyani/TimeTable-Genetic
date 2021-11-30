import random

from config import cfg
from genetic.field_state import FieldState


def _standard_reproduce(mom, dad):
    c1 = random.randint(0, len(cfg.course_list_all) - 1)
    c2 = random.randint(0, len(cfg.course_list_all) - 1)
    c2 = (c1 + c2) % len(cfg.course_list_all)
    if c2 < c1:
        c1, c2 = c2, c1
    temp = mom.arr[c1:c2 + 1]
    mp = {x: 1 for x in temp}
    arr = []
    for x in dad.arr:
        if x not in mp:
            arr.append(x)
    return FieldState(arr[:c1] + temp + arr[c1:])


def _mutate(child):
    x = random.randint(0, 99)
    if x < 10:
        c1 = random.randint(0, len(cfg.course_list_all) - 1)
        c2 = random.randint(0, len(cfg.course_list_all) - 1)
        child.arr[c1], child.arr[c2] = child.arr[c2], child.arr[c1]
        child.fitness = child.get_fitness_score()
    return child


def _get_parents(population):
    offset = min([person.fitness for person in population])
    if offset > 100:
        offset -= 20
    weights = [person.fitness - offset for person in population]
    return random.choices(population, weights, k=2)


def _pop_generator(population_size, population, mutate_func, rep_func):
    new_pop = []
    for i in range(population_size):
        mom, dad = _get_parents(population)
        child = rep_func(mom, dad)
        child = mutate_func(child)
        new_pop.append(child)
    return new_pop


def _genetic_algorithm(population_size, population, mutate_func, rep_func, times):
    generations = [population[0].fitness]
    global_max = population[0].fitness
    path = population[0]

    for i in range(times):
        population = _pop_generator(population_size, population, mutate_func, rep_func)
        most_fit_person_fitness = max([person.fitness for person in population])
        if most_fit_person_fitness >= global_max:
            global_max = most_fit_person_fitness
            for person in population:
                if person.fitness == global_max:
                    path = person
        generations.append(most_fit_person_fitness)
        print(f"Generation {i}'s most fit person has fitness {most_fit_person_fitness}")
        print(f"Best path till now: {path.arr} | Fitness Score: {path.fitness}")
    return generations, path


def start(epochs):
    population_size = 20
    population = [FieldState([i for i in range(len(cfg.course_list_all))]) for i in range(population_size)]
    return _genetic_algorithm(20, population, _mutate, _standard_reproduce, epochs)
