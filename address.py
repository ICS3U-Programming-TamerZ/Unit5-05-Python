#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 07, 2022
# This program gets a users address and formats it according to ontarios address
# laws.


def format_address(
    user_name, street_num, street_name, city, province, postal_code, apartment_num=None
):

    # Full address if user did not input an Apartment.
    if apartment_num == None:
        full_address = (
            f"{user_name}\n{street_num} {street_name}\n{city} {province} {postal_code}"
        )
        return full_address.upper()
    # Full address if user did input an Apartment.
    elif apartment_num != None:
        full_address = f"{user_name}\n{street_num} {street_name} {apartment_num}\n{city} {province} {postal_code}"
        return full_address.upper()


def main():
    # Initializes apartment to Null.
    apartment_num = None
    question = input("Do you live in an apartment (y or n): ")
    user_name = input("Please enter your name: ")
    # Gets users apartment number.
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_num = input("Please enter your apartment number (Unit/App): ")
    # Gets street num name, province city and postal code.
    street_num = input("Please enter a street number: ")
    street_name = input("Please enter a street name: ")
    city = input("Please enter your city: ")
    province = input("please enter a province: ")
    postal_code = input("Please enter your postal code: ")

    # Passes variables to function if apartment num was not given.
    if apartment_num == None:
        full_address = (format_address)(
            user_name,
            street_num,
            street_name,
            city,
            province,
            postal_code,
        )
    # Passes variables to function if apartment num was given.
    elif apartment_num != None:
        full_address = (format_address)(
            user_name,
            street_num,
            street_name,
            city,
            province,
            postal_code,
            apartment_num,
        )
    # Displays full address to user.
    print(full_address)


if __name__ == "__main__":
    main()
