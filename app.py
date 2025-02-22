import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load or Initialize Data
DATA_FILE = "growth_mindset_data.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["Date", "Learning", "Challenges Overcome"])

data = load_data()

# Set Page Configuration with Favicon
st.set_page_config(page_title="Growth Mindset Tracker", page_icon="🌟", layout="wide")  

# Custom Styling
st.markdown("""
    <style>
        body {background-color: #f5f5f5;}
        .title {
            text-align: center; 
            font-size: 50px;  
            font-weight: 800;  
            color: #1E90FF; 
            margin-bottom: 15px;
            text-transform: uppercase;
        }
        .section-title {
            font-size: 24px; 
            font-weight: bold; 
            color: #333; 
            margin-top: 30px;
            border-bottom: 3px solid #1E90FF;
            padding-bottom: 5px;
            width: 100%;
        }
        .data-box {
            background-color: white; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 3px 3px 12px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">Growth Mindset Tracker</p>', unsafe_allow_html=True)

# User Input Section
st.markdown('<p class="section-title">📌 Log Your Daily Progress</p>', unsafe_allow_html=True)
with st.container():
    date = st.date_input("Select Date")
    learning = st.text_area("What did you learn today?")
    challenge = st.text_area("What challenges did you overcome?")
    
    if st.button("Save Entry"):  
        new_data = pd.DataFrame({"Date": [date], "Learning": [learning], "Challenges Overcome": [challenge]})
        data = pd.concat([data, new_data], ignore_index=True)
        data.to_csv(DATA_FILE, index=False)
        st.success("✅ Entry Saved Successfully!")

# Display Learning Progress
st.markdown('<p class="section-title">📊 Your Learning Journey</p>', unsafe_allow_html=True)
with st.container():
    if not data.empty:
        st.markdown('<div class="data-box">', unsafe_allow_html=True)
        st.write(data.tail(5))  # Show last 5 entries
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization
        if "Date" in data and not data["Date"].isnull().all():
            fig, ax = plt.subplots(figsize=(6, 3))  # SMALLER GRAPH SIZE
            ax.plot(pd.to_datetime(data["Date"]), range(len(data)), marker="o", linestyle="-", color="blue")
            ax.set_xlabel("Date", fontsize=10)  # SMALLER LABEL
            ax.set_ylabel("Entries Logged", fontsize=10)  # SMALLER LABEL
            ax.set_title("Growth Over Time", fontsize=14, fontweight="bold")  # SMALLER TITLE
            plt.xticks(fontsize=8)  # SMALL X-TICKS
            plt.yticks(fontsize=8)  # SMALL Y-TICKS
            st.pyplot(fig)
        else:
            st.info("No valid date entries to plot yet.")
    else:
        st.info("No entries found. Start tracking today!")
