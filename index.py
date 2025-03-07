import streamlit as st

# Set Streamlit page configuration for better responsiveness
st.set_page_config(page_title="Google Unit Converter", page_icon="🔄", layout="wide")

# Apply responsive CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #F4F4F4;
            color: #333;
        }

        .stApp {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Responsive Title */
        .title {
            text-align: center;
            font-size: 4vw; /* Adjusts based on screen size */
            font-weight: 700;
            color: #2C3E50;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498DB;
            margin-bottom: 20px;
        }

        /* Subheading Styling */
        .subheading {
            text-align: center;
            font-size: 2.5vw;
            font-weight: 500;
            color: #555;
            margin-bottom: 15px;
        }

        /* Button styling */
        .stButton>button {
            background: #3498DB;
            color: white;
            font-weight: bold;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background: #2980B9;
            transform: scale(1.05);
            box-shadow: 0px 4px 8px rgba(52, 152, 219, 0.5);
        }

        /* Card styling with responsive padding */
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Make headings responsive */
        @media screen and (max-width: 600px) {
            .title { font-size: 6vw; } /* Bigger on mobile */
            .subheading { font-size: 4vw; }
        }
    </style>
""", unsafe_allow_html=True)

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

# Title with responsiveness
st.markdown("<h1 class='title'>🔄 Google-Style Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheading'>Convert units seamlessly</h3>", unsafe_allow_html=True)

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
st.markdown("<p style='text-align: center; font-size: 14px; color: #666;'>🚀 Built with Python & Streamlit</p>", unsafe_allow_html=True)
