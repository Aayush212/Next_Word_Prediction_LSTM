import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set page configuration
st.set_page_config(
    page_title="Next Word Predictor",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load the LSTM model
model = load_model('next_word_lstm.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

# Streamlit app
st.image("https://via.placeholder.com/800x200?text=Next+Word+Prediction+App", use_container_width=True)

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🔮 Next Word Prediction with LSTM</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style='text-align: center; color: gray;'>
    Enter a sequence of words, and let the magic of LSTM predict the next word! 🧙‍♂️
    </p>
    """,
    unsafe_allow_html=True,
)

# User input
input_text = st.text_input("Enter the sequence of words:", "To be or not to be")

if st.button("Predict Next Word ✨"):
    max_sequence_len = model.input_shape[1] + 1
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    if next_word:
        st.success(f"Predicted Next Word: **{next_word}**")
    else:
        st.error("Could not predict the next word. Please try a different input.")

# Add a footer
st.markdown(
    """
    <hr>
    <footer style='text-align: center; color: gray;'>
    © 2025 Next Word Prediction App | Built with ❤️ using Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)
