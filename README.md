# Healthcare Assistant Chatbot

## Overview
The Healthcare Assistant Chatbot is an AI-powered chatbot built with Streamlit, Hugging Face Transformers, and NLTK. It provides basic healthcare guidance on symptoms, medications, and doctor appointments using a DistilGPT-2 model and predefined responses. This chatbot offers an interactive experience through a user-friendly dark-themed UI.

## Features
- AI-powered responses using a pre-trained DistilGPT-2 model
- Predefined answers for common healthcare-related queries
- User-friendly dark-themed interface with Streamlit
- Text preprocessing with NLTK

## Prerequisites
Before running the chatbot, ensure you have the following installed:

- **Python (<= 3.12)** (TensorFlow is not currently compatible with Python 3.13 but may be updated in future versions)
- **Streamlit** (`pip install streamlit`)
- **Transformers** (`pip install transformers`)
- **NLTK** (`pip install nltk`)
- **Storage >= 5gb** to save the bot and modules locally 

Additionally, download necessary NLTK data before running the script:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Installation & Usage
1. Clone the repository or download the script.
2. Install the required dependencies using:
   ```sh
   pip install streamlit transformers nltk
   ```
3. Run the chatbot with:
   ```sh
   streamlit run main.py
   ```
4. Interact with the chatbot through the web interface.

## Notes
- This chatbot provides general guidance and should not replace professional medical advice.
- TensorFlow compatibility with Python 3.13 is currently unstable but may be updated in future versions.

## License
This project is open-source and free to use.

---
Feel free to modify this README based on additional features or updates to the project!



