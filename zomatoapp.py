import streamlit as st
import pandas as pd
import pickle
import google.generativeai as genai
from PIL import Image

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Lenovo\Downloads\project 6\Zomato_cluster_data.csv")
    return df

@st.cache_resource
def load_model():
    with open(r"C:\Users\Lenovo\Downloads\project 6\kmeans_model.pkl", 'rb') as file:
        kmeans = pickle.load(file)
    with open(r"C:\Users\Lenovo\Downloads\project 6\onehot_encoder.pkl", 'rb') as file:
        encoder = pickle.load(file)
    return kmeans, encoder

df = load_data()
kmeans, encoder = load_model()

# Function to get response from Google Generative AI using chat
def get_gemini_response(user_question):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": "Hello"},
                {"role": "model", "parts": "Great to meet you. What would you like to know?"}
            ]
        )
        response = chat.send_message(user_question)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while getting the response: {e}")
        return None

# Streamlit UI
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f0f0f0;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    .recommendation {
        border: 1px solid #2980b9;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        background-color: #ffffff;
    }
    .chatbot-response {
        border: 1px solid #2980b9;
        border-radius: 10px;
        padding: 10px;
        background-color: #ffffff;
    }
    .restaurant-name { color: #e74c3c; font-weight: bold; } /* Red for Restaurant Name */
    .rating { color: #f1c40f; font-weight: bold; } /* Yellow for Rating */
    .location { color: #3498db; font-weight: bold; } /* Blue for Location */
    .price { color: #27ae60; font-weight: bold; } /* Green for Price */
    .cuisine { color: #9b59b6; font-weight: bold; } /* Purple for Cuisines */
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍴 DineMate Recommendation App 🍴")

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Recommendations", "Map", "Chatbot"])

if page == "Recommendations":
    # Sidebar inputs
    st.sidebar.header("Search Options")
    cuisine_input = st.sidebar.text_input("Search Cuisines (comma-separated)", placeholder="Type cuisine names...")
    location_input = st.sidebar.selectbox("Select Location", options=df['City'].unique())
    rating_input = st.sidebar.slider("Select Rating", min_value=1.0, max_value=5.0, value=(1.0, 5.0), step=0.1)

    if st.sidebar.button("Get Recommendations"):
        if cuisine_input:
            cuisine_list = [cuisine.strip() for cuisine in cuisine_input.split(',') if cuisine.strip()]
            recommendations = df[df['City'] == location_input]
            recommendations = recommendations[recommendations['Cuisines'].str.contains('|'.join(cuisine_list), case=False, na=False)]
            recommendations = recommendations[(recommendations['Aggregate_rating'] >= rating_input[0]) & (recommendations['Aggregate_rating'] <= rating_input[1])]
        else:
            recommendations = df[(df['City'] == location_input) & (df['Aggregate_rating'] >= rating_input[0]) & (df['Aggregate_rating'] <= rating_input[1])]

        recommendations = recommendations.reset_index(drop=True)
        num_recommendations = len(recommendations)
        st.write(f"Number of recommendations found: {num_recommendations}")

        if not recommendations.empty and all(col in recommendations.columns for col in ['Restaurant_name', 'Cuisines', 'Aggregate_rating', 'City', 'Average_Cost_for_two', 'Currency']):
            for index, row in recommendations.iterrows():
                st.markdown(f"""
                <div class="recommendation">
                    <h3 class="restaurant-name">{row['Restaurant_name']} 🍴</h3>
                    <p><span class="cuisine"><strong>Cuisines:</strong> {row['Cuisines']} 🍽️</span></p>
                    <p><span class="rating"><strong>Rating:</strong> {row['Aggregate_rating']} ✨</span></p>
                    <p><span class="location"><strong>Location:</strong> {row['City']} 📍</span></p>
                    <p><span class="price"><strong>Average Cost for Two:</strong> {row['Average_Cost_for_two']} {row['Currency']} 🪙</span></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No recommendations found. Please try different inputs.")

elif page == "Map":
    st.sidebar.header("Restaurant Map")
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        st.markdown("<h2 style='text-align: center;'>Restaurant Locations on Map</h2>", unsafe_allow_html=True)
        map_data = df[['Restaurant_name', 'Latitude', 'Longitude']].rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
        st.map(map_data)
    else:
        st.write("Latitude and Longitude data is not available in the dataset.")

elif page == "Chatbot":
    st.sidebar.header("Chatbot")
    api_key = st.sidebar.text_input("Enter your Google Generative AI API Key:", type="password")
    user_question = st.sidebar.text_input("Ask a cooking-related question:")

    if st.sidebar.button("Ask"):
        if not api_key:
            st.write("Please enter your API key to use the chatbot.")
        else:
            genai.configure(api_key=api_key)
            cooking_keywords = ['recipe', 'cook', 'cooking', 'ingredient', 'bake', 'fry', 'grill', 'boil', 'sauté', 'meal', 'dish', 'food', 'prepare']
            if any(keyword in user_question.lower() for keyword in cooking_keywords):
                with st.spinner("Getting response..."):
                    try:
                        response = get_gemini_response(user_question)
                        if response:
                            st.markdown(f"<div class='chatbot-response'>{response}</div>", unsafe_allow_html=True)
                        else:
                            st.write("I'm sorry, but I couldn't find an answer. Please try asking something else.")
                    except Exception as e:
                        st.write(f"An error occurred: {e}")
            else:
                st.write("Please ask a cooking-related question.")