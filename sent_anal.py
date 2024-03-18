import streamlit as st
import joblib

# Load the trained model
model = joblib.load('/Users/mehakassim/Desktop/sentiment_analysis_model.pkl')

# Define the Streamlit app
def main():
    st.title('Sentiment Analysis App')

    # User input
    user_input = st.text_area('Enter your text here:')
    if st.button('Predict'):
        prediction = model.predict([user_input])
        st.write('Prediction:', prediction)
        
        
# Run the app
if __name__ == '__main__':
    main()