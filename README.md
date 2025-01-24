# Next_Word_Prediction_LSTM

This repository contains the code for a **Next Word Prediction** application built using **Streamlit** and an **LSTM (Long Short-Term Memory)** model. The app predicts the next word in a given sequence of text based on the trained LSTM model and a tokenizer.

## Features
- Predicts the next word for a given text input.
- Interactive web-based interface using Streamlit.
- Supports dynamic user input.
- Provides immediate feedback with success or error messages.

## How It Works
1. The user enters a sequence of words into the text input field.
2. The app processes the input using a trained LSTM model and a tokenizer.
3. The predicted next word is displayed to the user.

## Live Demo
Try the app live on Streamlit:
[Next Word Prediction App](---------------------------------------)

## Installation
To run the app locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/next-word-prediction-app.git
   cd next-word-prediction-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pretrained LSTM model (`next_word_lstm.h5`) and tokenizer pickle file (`tokenizer_pickle`) and place them in the root directory of the project.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

## File Structure
```
next-word-prediction-app/
├── app.py               # Main Streamlit application
├── next_word_lstm.h5    # Pretrained LSTM model
├── tokenizer_pickle     # Tokenizer pickle file
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
```

## Dependencies
- Python 3.8+
- Streamlit
- TensorFlow
- NumPy
- Pickle

Install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Example Usage
1. Enter a sequence of words (e.g., `"To be or not to be"`).
2. Click on the **Predict Next Word** button.
3. The predicted next word will be displayed below the button.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the app.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for providing an excellent framework for building web apps.
- TensorFlow for enabling powerful machine learning capabilities.

## Author
[Aayush Mishra](https://github.com/Aayush212)

