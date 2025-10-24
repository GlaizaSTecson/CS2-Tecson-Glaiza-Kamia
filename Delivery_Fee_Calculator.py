def calculate_delivery_fee(distance, rate):
    return distance * rate
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))
total_fee = calculate_delivery_fee(distance, rate)
print(f"Total Delivery Fee: ₱{total_fee:.2f}")
