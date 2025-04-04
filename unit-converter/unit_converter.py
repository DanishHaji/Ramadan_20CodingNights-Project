import streamlit as st

def convert_units(value, from_unit, to_unit):
    """
    Convert a value from one unit to another.
    """
    conversion_factors = {
        'meter_to_kilometer': 0.001, # 1 meter = 0.001 kilometers
        'kilometer_to_meter': 1000, # 1 kilometer = 1000 meters
        'gram_to_kilogram': 0.001,  # 1 gram = 0.001 kilograms
        'kilogram_to_gram': 1000,   # 1 kilogram = 1000 grams
    }

    key = f"{from_unit}_to_{to_unit}"

    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        return "Conversion not supported"

st.title("Unit Converter")
st.write("Convert between different units of measurement.")
value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the unit to convert from:", ["meter", "kilometer", "gram", "kilogram"])
to_unit = st.selectbox("Select the unit to convert to:", ["meter", "kilometer", "gram", "kilogram"])
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
