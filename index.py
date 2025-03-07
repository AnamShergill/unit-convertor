import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Google Unit Converter", page_icon="🔄", layout="centered")

# Apply custom neon theme CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&display=swap');

        body {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: #ffffff;
        }

        .stApp {
            background: transparent;
            padding: 2rem;
        }

        /* Neon Title */
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: 800;
            color: #00ffff; /* Neon Cyan */
            text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #ff00ff;
            padding-bottom: 10px;
            border-bottom: 4px solid #ff00ff; /* Neon Pink Border */
            margin-bottom: 20px;
        }

        /* Button styling */
        .stButton>button {
            background: #ff00ff;
            color: white;
            font-weight: bold;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        }

        .stButton>button:hover {
            background: #00ffff;
            transform: scale(1.1);
            box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
        }

        /* Card styling */
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 255, 255, 0.3);
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }

    </style>
""", unsafe_allow_html=True)

# Title (with updated styles)
st.markdown("<h1 class='title'>🔄 Google-Style Unit Converter</h1>", unsafe_allow_html=True)

# Define unit conversion dictionary
conversions = {
    "Length": {
        "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701
    },
    "Weight": {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, 
        "Fahrenheit": lambda x: (x * 9/5) + 32, 
        "Kelvin": lambda x: x + 273.15
    }
}

# Function to convert units
def convert_units(value, from_unit, to_unit, category):
    if from_unit == to_unit:
        return value  # No conversion needed

    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return round((value * 9/5) + 32, 2)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return round(value + 273.15, 2)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return round((value - 32) * 5/9, 2)
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return round(((value - 32) * 5/9) + 273.15, 2)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return round(value - 273.15, 2)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return round(((value - 273.15) * 9/5) + 32, 2)

    # Standard unit conversion
    base_value = value / conversions[category][from_unit]
    converted_value = base_value * conversions[category][to_unit]

    return round(converted_value, 4)

# Card-style layout
st.markdown("<div class='card'>", unsafe_allow_html=True)

# Dropdown for unit category
category = st.selectbox("Select Category:", list(conversions.keys()))

# Dropdowns for unit selection
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert from:", list(conversions[category].keys()))
with col2:
    to_unit = st.selectbox("Convert to:", list(conversions[category].keys()))

# Input field for value
value = st.number_input("Enter Value:", min_value=-1000.0, max_value=100000.0, step=0.1)

# Convert button
if st.button("🔄 Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"✅ Converted Value: **{result} {to_unit}**")

# Close card
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #bbb;'>🚀 Built with Python & Streamlit</p>", unsafe_allow_html=True)
