# Modifying the get_user_inputs function to include an additional prompt for the average number of months a full gas tank lasts


def get_user_inputs():
    full_tank_cost = float(
        input(
            "How much it is to fully fill your gas tank if it is fully empty? (in your currency): "
        )
    )
    hourly_wage = float(input("What is your hourly wage? (in your currency): "))
    currency = input("What is your currency? ")

    # New input for the average number of months a full tank lasts
    avg_months_last = float(
        input(
            "On average, how many months does a fully filled gas tank last? (Enter a number not bigger than 12): "
        )
    )

    while avg_months_last > 12:
        avg_months_last = float(input("Please enter a number not bigger than 12: "))

    annual_interest_rate = float(
        input("Annual interest rate in your country right now?: ")
    )
    return full_tank_cost, hourly_wage, currency, avg_months_last, annual_interest_rate


def find_optimal_cost(
    full_tank_cost,
    avg_months_last,
    interest_rate,
    hourly_wage,
    tolerance,
    minitues_to_travel_and_back,
):
    # Calculate initial EOQ
    D = (12 / avg_months_last) * full_tank_cost  # Annual demand
    S = full_tank_cost  # Initial cost per order
    H = (
        ((full_tank_cost / 400) + (hourly_wage / (60 / minitues_to_travel_and_back)))
        * (1 / interest_rate) ** (12**0.5)
    ) * (
        interest_rate / 2
    )  # Holding cost

    EOQ = (2 * D * S / H) ** 0.5

    # Iterate to adjust S until EOQ is close enough to S
    while abs(EOQ - S) > tolerance:
        # Adjust S (e.g., decrease by a small percentage)
        S *= 0.99  # Decrease S by 1%

        # Recalculate EOQ with the new S
        EOQ = (2 * D * S / H) ** 0.5

        # Ensure we don't surpass the full tank cost
        if S < full_tank_cost:
            break

    return D, H, EOQ


# Example usage
# optimal_cost, optimal_eoq = find_optimal_cost(full_tank_cost, avg_months_last, annual_interest_rate)


# Example usage
# full_tank_cost, hourly_wage, currency, avg_months_last = get_user_inputs()
# D, S, H = calculate_inventory_parameters(full_tank_cost, avg_months_last, hourly_wage)


# The main function remains the same, with an addition to accommodate the new input


def main():
    minitues_to_travel_and_back = 15
    # Get user inputs
    (
        full_tank_cost,
        hourly_wage,
        currency,
        avg_months_last,
        annual_interest_rate,
    ) = get_user_inputs()

    # Calculate inventory parameters
    D, H, EOQ = find_optimal_cost(
        full_tank_cost,
        avg_months_last,
        annual_interest_rate,
        hourly_wage,
        tolerance=0.01,
        minitues_to_travel_and_back=minitues_to_travel_and_back,
    )

    # Print the inputs
    print(f"Full Tank Cost: {full_tank_cost} {currency}")
    print(f"Hourly Wage: {hourly_wage} {currency}/hour")
    print(f"Average Months a Full Tank Lasts: {avg_months_last} months")
    print(f"Annual Interest Rate: {annual_interest_rate}")

    # Print the calculated outputs
    print(f"\nCalculated Values:")
    print(f"Annual Demand (D): {D} {currency}")

    print(f"Oportunity Cost (H): {H} {currency}")
    if hourly_wage > 2500:  # 500000 in monthly wage
        print(f"Get a driver bro")
    elif EOQ < full_tank_cost:
        print(
            f"So you must pay: {EOQ} {currency} to achive the optimal amount of gas in your tank this equates to {EOQ/full_tank_cost} of a full tank."
        )
        print(
            f"Which is {hourly_wage * (full_tank_cost - EOQ) / 12 / avg_months_last} {currency} per year as a result of this strategy in terms of eliminating opportunity cost"
        )
        N = D / EOQ
        if_not = D / full_tank_cost
        print(
            f"Number of visits to gas station in a year if we follow this strategy {N}"
        )
        print(
            f"Number of hours spent at gas station if we follow this strategy {(N+2)*(minitues_to_travel_and_back/60)}"  # 15 minutes spent in gas station to fill the tank and 2 minutes on average to go to gas station because we decide to get gas on the go so no return time
        )
        print(
            f"\nIf you fill your tank fully, you would have {if_not} visits to gas station in a year"
        )
        print(
            f"Number of hours spent at gas station if you fill your tank fully {if_not*minitues_to_travel_and_back/60}"
            f"\n{minitues_to_travel_and_back*(if_not*minitues_to_travel_and_back/60)} hours spend to go to gas station if you fill your tank fully when emptied"
            f"\nTotal {(if_not+(if_not*minitues_to_travel_and_back))*(minitues_to_travel_and_back/60)} hours spend to go to gas station and to fill if you fill your tank fully when emptied"
            f"\nThis much hour can be saved if you buy gas the optimal amount when you see a gas station: {((if_not+(if_not*minitues_to_travel_and_back))*(minitues_to_travel_and_back/60))-(N+2)*(minitues_to_travel_and_back/60)}"
        )
        print(
            f"\nSo you will go to gas station to fill your tank {if_not} times at minimum and each time you go should buy minumum {EOQ} {currency} of gas each time"
        )
        print(
            f"\nAfter your tank fullness level drops to {1-(EOQ/full_tank_cost)} you shuld stop and fill at least {EOQ} {currency} of gas each time\n"
        )
    else:
        print(f"You should always fill your tank fully.")


if __name__ == "__main__":
    main()
