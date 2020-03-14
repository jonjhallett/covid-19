#!/bin/python3 -tt

import math

deaths_in_uk = 21

population_of_uk = 66400000
fatality_rate = 0.009
doubling_rate_in_days = 6.2
average_time_to_death_in_days = 17.3


def main():
    for number_of_people in [350, 700, 1400, 3500, 35000]:
        probability = probability_of_at_least_one_case(number_of_people)
        print(f'{number_of_people}\t{probability:0.2f}')


def deaths_to_true_cases(number_of_deaths):
    cases_to_deaths_factor = 1 / fatality_rate
    time_from_initial_infection_to_death_factor = 2 ** (average_time_to_death_in_days / doubling_rate_in_days)

    true_number_of_cases = number_of_deaths * cases_to_deaths_factor * time_from_initial_infection_to_death_factor

    return true_number_of_cases


def probability_of_at_least_one_case(number_of_people):
    true_cases_in_uk = deaths_to_true_cases(deaths_in_uk)

    probability_of_no_cases = 1
    for i in range(0, number_of_people):
        unsampled_population = population_of_uk - i
        probability_of_no_cases *= (unsampled_population - true_cases_in_uk) / unsampled_population

    probability_of_at_least_one_case = 1 - probability_of_no_cases
    return probability_of_at_least_one_case


main()
