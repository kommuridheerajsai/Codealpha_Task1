# CodeAlpha_Task1_Language_Translation_Tool

##  Project Title

Language Translation Tool using Python and Streamlit

##  Project Description

This project is developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The Language Translation Tool allows users to enter text, select a source language, choose a target language, and translate the text instantly. The project uses a translation API/library to process the input text and display the translated output clearly on the screen.

It also includes an optional text-to-speech feature that converts the translated text into audio for better usability.

##  Objectives

* Create a simple user interface for text translation.
* Allow users to enter text.
* Allow users to select source and target languages.
* Translate text using a translation API/library.
* Display the translated text clearly.
* Add text-to-speech support for translated output.

##  Technologies Used

* Python
* Streamlit
* Google Translator Library
* gTTS

##  Libraries Used

```bash
streamlit
deep-translator
gtts
```

##  Installation

###  Install Required Libraries

```bash
python -m pip install streamlit deep-translator gtts
```

##  How to Run

Run the project using:

```bash
python -m streamlit run language_translation_tool.py
```

After running the command, Streamlit will open the application in your browser.

##  Working Process

1. The user enters text in the input box.
2. The user selects the source language.
3. The user selects the target language.
4. The text is sent to the translation library.
5. The translated text is received.
6. The translated output is displayed on the screen.
7. The translated text is converted into audio using text-to-speech.

##  Project Flow

```text
User Input Text
      ↓
Select Source Language
      ↓
Select Target Language
      ↓
Send Text to Translation API
      ↓
Receive Translated Text
      ↓
Display Translated Output
      ↓
Play Audio Output
```

##  Features

* Simple and user-friendly interface.
* Supports multiple languages.
* Translates text instantly.
* Displays translated text clearly.
* Includes text-to-speech feature.
* Easy to run using Streamlit.

##  Supported Languages

* English
* Hindi
* Telugu
* Tamil
* Kannada
* Malayalam
  
##  Output

The application displays:

* Input text box
* Source language selection
* Target language selection
* Translate button
* Translated text output
* Audio output for translated text

##  Future Improvements

* Add a copy button for translated text.
* Add more languages.
* Add speech-to-text input.
* Improve user interface design.
* Add translation history.
* Deploy the app online.

## 🏁 Conclusion

This project successfully demonstrates a language translation tool using Python and Streamlit. It helps users translate text from one language to another and improves usability by providing audio output using text-to-speech.

# Screenshot
```
Screenshot 2026-06-13 105526.png
```
##  Author

**Dheeraj Sai Kommuri**

##  Internship

**CodeAlpha Artificial Intelligence Internship**
