def calculate_do2(cardiac_output, arterial_oxygen_content):
    """
    Calculate Oxygen Delivery (DO2) in actual conditions.
    
    :param cardiac_output: Cardiac output in liters per minute (L/min)
    :param arterial_oxygen_content: Arterial oxygen content in milliliters of oxygen per deciliter of blood (mL/dL)
    :return: Oxygen Delivery (DO2) in milliliters of oxygen per minute (mL/min)
    """
    do2 = cardiac_output * arterial_oxygen_content * 10 # Convert from mL/dL to mL/L
    return do2

# Example usage
cardiac_output = 5.0 # L/min
arterial_oxygen_content = 20.0 # mL/dL

oxygen_delivery = calculate_do2(cardiac_output, arterial_oxygen_content)
print("Oxygen Delivery (DO2): {} mL/min".format(oxygen_delivery))
