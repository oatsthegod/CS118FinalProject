""" Program will find best route, maxing out a given budget, and can adapt to all changes made to data sets."""

from itertools import permutations, combinations_with_replacement

# initializing variables and lists for later use
best_route_hotel_list = None
best_max_budget = None
budget = 850
final_route = None
final_max_temp = None
city_with_temp = {
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Casa Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
}
hotel_with_price = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209,
}
hotel_list = list(hotel_with_price.keys())  # making a list of the hotel names

temp_save = list()
temp_save.append(30)
permutations_of_hotel_name = combinations_with_replacement(hotel_list, len(city_with_temp)+1)
for combination_hotel in list(permutations_of_hotel_name):  # for loop to create list of combinations of hotels
    temp_list_hotel = list(combination_hotel)
    temp_list_hotel = temp_list_hotel[:-1]

    extract_price = [hotel_with_price[i] for i in temp_list_hotel]
    total_count = sum(extract_price)
    difference_price = budget - total_count  # finding the options which fall under 850 dollars
    if difference_price < 0:
        continue

    temp_save.append(difference_price)

    calculate_minimum = min(temp_save)  # finding ideal route by finding the lowest difference in price and our budget

    if calculate_minimum == difference_price:  # if the lowest value matches the difference in price, it will save the
        lowest_price = difference_price   # current list to best_route_hotel_list and best_max_budget
        temp_save = temp_save[1:]
        best_max_budget = total_count
        best_route_hotel_list = temp_list_hotel

    else:
        temp_save = temp_save[:-1]  # if not, it removes the last index, and makes a new list to iterate over


number_of_max_temps = None
for city_name, list_temperature in city_with_temp.items():  # getting the number of max temps in each city
    number_of_max_temps = len(list_temperature)

if number_of_max_temps:
    city_list = list(city_with_temp.keys())  # getting a list of the cities

    permutations_of_city_name = permutations(city_list)

    temp_list_for_max_temperature = list()  # initializing list for max temp
    for variation in list(permutations_of_city_name):
        variation_list = list(variation)

        list_according_day_temperature = [city_with_temp[x][i] for i, x in enumerate(variation_list)]  # listing all
        # max temps in a day per city
        average_temp_list = sum(list_according_day_temperature) / number_of_max_temps  # getting average
        # temp of all cities

        temp_list_for_max_temperature.append(average_temp_list)
        if len(temp_list_for_max_temperature) != 1:  # when the list is longer than 1 or empty
            max_temp = max(temp_list_for_max_temperature)  # max temperature is the maximum of the temp list
            if max_temp == average_temp_list:  # if the max temp list is equal to the avg temp list
                final_max_temp = average_temp_list  # that is the highest average temperature
                final_route = variation_list  # takes the highest temperature route and saves as best route
                temp_list_for_max_temperature = temp_list_for_max_temperature[1:]

            else:
                temp_list_for_max_temperature = temp_list_for_max_temperature[:-1]  # if not, it removes the last
                # index, and makes a new list to iterate over
if __name__ == "__main__":
    print(f'Here is your best route: {final_route} the average of the daily max temp. is {final_max_temp}F')
    print(f'To max out your hotel budget, stay at these hotels: {best_route_hotel_list}, totaling ${best_max_budget}')
