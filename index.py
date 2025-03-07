import streamlit as st

# Set Streamlit page configuration for a better layout
st.set_page_config(page_title="Google Unit Converter", page_icon="🔄", layout="wide")

# Apply custom CSS for a dark theme with improved visibility
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #141E30, #243B55); /* Dark Gradient */
            color: #EAECEE;
        }

        .stApp {
            background: transparent;
            padding: 2rem;
        }

        /* Title Styling */
        .title {
            text-align: center;
            font-size: 4vw;
            font-weight: 700;
            color: #F39C12; /* Bright orange for visibility */
            padding-bottom: 10px;
            border-bottom: 3px solid #F39C12;
            margin-bottom: 20px;
        }

        /* Subheading Styling */
        .subheading {
            text-align: center;
            font-size: 2.5vw;
            font-weight: 500;
            color: #F1C40F; /* Light yellow for contrast */
            margin-bottom: 15px;
        }

        /* Card Styling */
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }

        /* Button Styling */
        .stButton>button {
            background: #F39C12;
            color: white;
            font-weight: bold;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background: #E67E22;
            transform: scale(1.05);
            box-shadow: 0px 4px 8px rgba(243, 156, 18, 0.5);
        }

        /* Mobile-friendly Adjustments */
        @media screen and (max-width: 600px) {
            .title { font-size: 6vw; } 
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

# Title
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
st.markdown("<p style='text-align: center; font-size: 14px; color: #BDC3C7;'>🚀 Built with Python & Streamlit</p>", unsafe_allow_html=True)
