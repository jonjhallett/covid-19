#!/bin/python3 -tt

import math

def main():
    population_of_uk = 66400000
    deaths_in_uk = 10
    true_cases_in_uk = deaths_to_true_cases(deaths_in_uk)
    print(f'True number of cases = {true_cases_in_uk:0.2f}')

    number_people_in_ggs = 350
    probability_of_no_cases_in_ggs = 1
    for i in range(0, number_people_in_ggs):
        probability_of_no_cases_in_ggs *= (population_of_uk - true_cases_in_uk - i) / (population_of_uk - i)

    probability_of_at_least_one_case_in_ggs = 1 - probability_of_no_cases_in_ggs
    print(f'{probability_of_at_least_one_case_in_ggs:0.2f}')

def deaths_to_true_cases(number_of_deaths):
    fatality_rate = 0.009
    doubling_rate_in_days = 6.2
    average_time_to_death_in_days = 17.3

    base_multiplier = 1 / fatality_rate
    delay_factor = 2 ** (average_time_to_death_in_days / doubling_rate_in_days)
    print(f'Delay factor = {delay_factor:.2f}')

    true_number_of_cases = number_of_deaths * base_multiplier * delay_factor

    return true_number_of_cases

main()
