# Oxygen Delivery (DO2) Calculator

This repository contains a Python code for calculating the Oxygen Delivery (DO2) in actual conditions. The DO2 is an important parameter used in medical settings to assess the amount of oxygen delivered to tissues per unit of time.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Explanation](#explanation)
- [How to Run](#how-to-run)
- [Follow Me](#follow-me)

## Introduction
Oxygen Delivery (DO2) is a crucial metric in medical physiology that measures the amount of oxygen delivered to tissues per minute. It provides valuable information about the adequacy of oxygen supply to meet the metabolic demands of the body.

The DO2 is calculated by multiplying the cardiac output, which represents the volume of blood pumped by the heart per minute, with the arterial oxygen content, which indicates the concentration of oxygen in the arterial blood. By assessing the DO2, healthcare professionals can evaluate the oxygen-carrying capacity of the blood and identify any potential oxygenation issues.

## Usage
To use the Oxygen Delivery (DO2) calculator, follow these steps:

1. Set the values for `cardiac_output` and `arterial_oxygen_content` variables in the code.
2. Run the script.
3. The calculated DO2 value will be displayed in milliliters of oxygen per minute (mL/min).

Example usage:
```python
cardiac_output = 5.0 # L/min
arterial_oxygen_content = 20.0 # mL/dL

oxygen_delivery = calculate_do2(cardiac_output, arterial_oxygen_content)
print("Oxygen Delivery (DO2): {} mL/min".format(oxygen_delivery))
```

## Explanation
The Oxygen Delivery (DO2) is calculated using the following formula:

```
DO2 = cardiac_output * arterial_oxygen_content * 10
```

- `cardiac_output`: Cardiac output represents the volume of blood pumped by the heart per minute (L/min).
- `arterial_oxygen_content`: Arterial oxygen content indicates the concentration of oxygen in the arterial blood, measured in milliliters of oxygen per deciliter blood (mL/dL).

To convert the arterial oxygen content from mL/dL to mL/L, we multiply it by a conversion factor of 10.

The calculated DO2 represents the amount of oxygen delivered to tissues per minute and is expressed in milliliters of oxygen per minute (mL/min).

## How Run
To run the code, follow these steps:

1. Install Python on your system if it's not already installed. You can download Python from the official website: [Python.org](https://www.python.org/).
2. Clone this repository or download the `calculate_do2.py` file.
3. Open a terminal or command prompt and navigate to the directory where the `calculate_do2.py` file is located.
4. Run the following command to execute the script   ```
   python calculate_do2.py
   ```
5. Set the values for `cardiac_output` and `arterial_oxygen_content` variables in the code according to your requirements.
6. Press Enter to run the script.
7. The calculated Oxygen Delivery (DO2) value will be displayed in the console.

## Follow Me
If you find this code useful, feel free to follow me on LinkedIn and Twitter for more updates and resources:

LinkedIn: [Reza Eghbal](https://.linkedin.com/in/mreghbal)

Twitter: [Reza Eghbal](https://twitter.com/mreghbal)

Thank you for using the Oxygen Delivery (DO2) calculator!
