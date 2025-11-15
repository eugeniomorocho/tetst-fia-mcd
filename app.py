import streamlit as st

# App title shown at the top of the Streamlit app
st.title("💻 Frequency Plot from a slider")

# Slider widget to control frequency
frequency = st.slider("Select Frequency", 1, 10, 5)




# Run the app with:
# Step 1: Open your terminal
# Step 2: Install Streamlit if you haven't already:
#    pip install streamlit
# Step 3: Navigate to the directory containing this app.py file
# Step 4: Run the app with the command:
# streamlit run app.py