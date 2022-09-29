# calculation_to_hours = 24
# name_of_unit = "hours" = are going to be get from the user input.


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
      return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return"unsupported unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid Number")
        else:
            print("you have entered a Negative Number.")
    except ValueError:
        print("your input is not a valid number!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit!\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()

# my_list = ["20", "30", "40"]
# print(my_list[2])
#
#
# my_dictionary = {"days": 20, "unit": "hour"}
# print(my_dictionary["unit"])