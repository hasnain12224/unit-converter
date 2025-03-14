import streamlit as st

# App ka title
st.title("⚖️ Simple Unit Converter")

# Unit options list
units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Category select karne ka option
category = st.selectbox("Select Category:", list(units.keys()))

# "From" aur "To" unit select karne ke options
from_unit = st.selectbox("Convert From:", units[category])
to_unit = st.selectbox("Convert To:", units[category])

# User se value input lena
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Conversion logic
def convert(value, from_unit, to_unit):
    length_conversion = {
        "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34
    }
    weight_conversion = {
        "Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495
    }
    temperature_conversion = {
        "Celsius": lambda x: x, 
        "Fahrenheit": lambda x: (x - 32) * 5/9, 
        "Kelvin": lambda x: x - 273.15
    }

    if from_unit in length_conversion and to_unit in length_conversion:
        return value * (length_conversion[to_unit] / length_conversion[from_unit])
    
    elif from_unit in weight_conversion and to_unit in weight_conversion:
        return value * (weight_conversion[to_unit] / weight_conversion[from_unit])

    elif from_unit in temperature_conversion and to_unit in temperature_conversion:
        return temperature_conversion[to_unit](value)

    else:
        return "Invalid Conversion"

# Conversion result dikhana
if value:
    result = convert(value, from_unit, to_unit)
    st.write(f"🔹 {value} {from_unit} is equal to {result:.2f} {to_unit}")

