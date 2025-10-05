def convert_velocity(value, unit):
    unit = unit.lower()
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "km/s":
        return value * 1000
    elif unit == "mi/s":
        return value * 1609.34
    else:
        print("Unsupported velocity unit.")
        return None


def convert_acceleration(value, unit):
    unit = unit.lower()
    if unit == "m/s²" or unit == "m/s^2":
        return value
    elif unit == "ft/s²" or unit == "ft/s^2":
        return value * 0.3048
    elif unit == "km/s²" or unit == "km/s^2":
        return value * 1000
    elif unit == "mi/s²" or unit == "mi/s^2":
        return value * 1609.34
    else:
        print("Unsupported acceleration unit.")
        return None

def motion_type(v, a):
    if v == 0:
        return "At Rest"
    elif v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "Unknown Motion"
    
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)

m_type = motion_type(v_si, a_si)

print("\nResults:")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s²")
print(f"Motion Type = {m_type}")