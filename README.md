# Multilingual-Multigenre-Creative-Content-Chatbot
This project generates creative stories, poems, or songs based on user prompts, translates the content, creates related images, and can read the output aloud in multiple languages using Streamlit, LangChain, and OpenAI APIs.

**Multilingual-Multigenre-Creative-Content-Chatbot** is a versatile web application that generates creative content including stories, poems, and songs based on user prompts. Utilizing advanced language models and AI technologies, the app can also translate content, generate related images, and read the output aloud in various languages.

## Features
- **Creative Generation:** Create stories, poems, or songs in multiple genres and languages.
- **Translation:** Translate generated content into English and summarize it.
- **Image Generation:** Generate images related to the created content using OpenAI's DALL-E.
- **Text-to-Speech:** Read the generated content aloud in various languages using Google Text-to-Speech (gTTS).
- **Interactive User Interface:** User-friendly interface built with Streamlit for seamless interaction.

## Technologies Used
- **Streamlit:** For building the web application interface.
- **OpenAI API:** To generate text content and images.
- **LangChain:** To manage language model prompts and chains.
- **gTTS (Google Text-to-Speech):** For converting text to speech.
- **Requests:** For handling HTTP requests and responses.
- **PIL (Python Imaging Library):** For image processing.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/story-teller.git
   ```
2. Navigate to the project directory:
   ```bash
   cd story-teller
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8501` to access the app.

## How to Contribute
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a pull request.


## Acknowledgements
- OpenAI for their powerful language models.
- Streamlit for providing an excellent platform for web applications.
- Google for their Text-to-Speech technology.
