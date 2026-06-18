import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 Language Translation Tool")
st.write("Enter text, select source and target languages, and get the translated result.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",    
    "Gujarati": "gu",
    "Punjabi": "pa",
}

text = st.text_area("Enter text to translate:", height=150)

source_language = st.selectbox("Select Source Language:", list(languages.keys()))
target_language = st.selectbox("Select Target Language:", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    elif source_language == target_language:
        st.warning("Source and target languages are same. Please select different languages.")
    else:
        try:
            
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(text)

          
            st.success("Translated Text:")
            st.text_area("Output:", translated_text, height=150)

            
            tts = gTTS(text=translated_text, lang=languages[target_language])
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)

            st.audio(audio_file, format="audio/mp3")

        except Exception as e:
            st.error("Translation failed. Please check your internet connection.")
            st.write("Error:", e)