#!/bin/python3 -tt

import math

def main():
    for number_of_people in range(350, 1351, 100):
        probability = probability_of_at_least_one_case(number_of_people)
        print(f'{number_of_people}\t{probability:0.2f}')

def deaths_to_true_cases(number_of_deaths):
    fatality_rate = 0.009
    doubling_rate_in_days = 6.2
    average_time_to_death_in_days = 17.3

    base_multiplier = 1 / fatality_rate
    delay_factor = 2 ** (average_time_to_death_in_days / doubling_rate_in_days)

    true_number_of_cases = number_of_deaths * base_multiplier * delay_factor

    return true_number_of_cases

def probability_of_at_least_one_case(number_of_people):
    population_of_uk = 66400000
    deaths_in_uk = 10
    true_cases_in_uk = deaths_to_true_cases(deaths_in_uk)

    probability_of_no_cases = 1
    for i in range(0, number_of_people):
        probability_of_no_cases *= (population_of_uk - true_cases_in_uk - i) / (population_of_uk - i)

    probability_of_at_least_one_case = 1 - probability_of_no_cases
    return probability_of_at_least_one_case

main()
