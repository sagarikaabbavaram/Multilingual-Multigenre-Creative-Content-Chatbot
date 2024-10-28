import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
import openai 
import os
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLM
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.chat_models import ChatOpenAI
from gtts import gTTS
import time




load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  # Should not print the actual key in production
# Set the OpenAI API key
openai.api_key = api_key

with st.sidebar:
    options = ["Stroy", "Poem", "Song"]
    story = st.selectbox("I’m enthusiastic about...", options,index=None,)
    options = ["beautifull","Adventure", "Comedy", "Drama", "Fantasy", "Historical", "Horror", "Mystery", "Romance", "Science Fiction", "Thriller", "Tragedy", "Crime", "Folklore", "Satire", "Gothic", "Surrealism", "Magical Realism", "Suspense", "Realism",  "Mythology", "Epic", "Lyric", "Narrative", "Tragicomedy"]
    Genre = st.selectbox("What genre are you in the mood for?", options,index=None,)
    options = ["English","Hindi","Telugu","Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani", "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chinese", "Chinese", "Corsican", "Croatian", "Czech", "Danish", "Dutch", "Esperanto", "Estonian", "Finnish", "French", "Galician", "Georgian", "German", "Greek", "Gujarati", "Haitian Creole", "Hebrew" , "Hmong", "Hungarian", "Icelandic", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Kurdish", "Kyrgyz", "Lao", "Latvian", "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Maori", "Marathi", "Mongolian", "Nepali", "Norwegian", "Odia", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Samoan", "Scottish Gaelic", "Serbian", "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tajik", "Tamil", "Thai", "Turkish", "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"]
    language = st.selectbox("What language would you love to dive into?", options,index=None,)


prompt=PromptTemplate(
    input_variables=["Genre","input_text","language","story"], 
    template='''Act as a skilled and versatile writer capable of crafting meaningful and engaging stories, poems, and songs in multiple languages. For each request, use your creativity to bring vivid imagery, emotional depth, and clarity to the content, ensuring that the message is easy to understand. Genres may include romance, adventure, fantasy, mystery, sci-fi, horror, and comedy.

Deliver concise yet impactful narratives that resonate with the audience, focusing on key themes and ideas while ensuring the content is original, expressive, and semantically meaningful. Be mindful of keeping the response around 200 words, making it both clear and captivating.

Please create a {Genre} {story} in {language} about {input_text}, ensuring the output is meaningful, concise, and engaging.'''
)
#llm = OllamaLLM(model="llama3.2")
llm = ChatOpenAI(model_name="gpt-4",openai_api_key=api_key, temperature=0.7,streaming=True,callbacks=[StreamingStdOutCallbackHandler()])  # Enables continuous output


parser=StrOutputParser()
chain=LLMChain(
    llm=llm,
    prompt=prompt,
    output_parser=parser
)
st.title("🐥𝓢𝓽𝓸𝓻𝔂 𝓣𝓮𝓵𝓵𝓮𝓻 😊✨")
#st.header("₊✩‧₊˚𝓐 𝓦𝓸𝓻𝓵𝓭 𝓑𝓮𝔂𝓸𝓷𝓭 𝓦𝓸𝓻𝓭𝓼✮⋆˙")
st.subheader("✰⋆⁺₊⋆𝓛𝓮𝓽’𝓼 𝓭𝓲𝓿𝓮 𝓲𝓷𝓽𝓸 𝓽𝓱𝓮 𝓳𝓸𝔂!⋆⁺₊⋆✰")
result=""

def on_button_click():
    st.title("🐥𝓢𝓽𝓸𝓻𝔂 𝓣𝓮𝓵𝓵𝓮𝓻 😊✨")
#st.header("₊✩‧₊˚𝓐 𝓦𝓸𝓻𝓵𝓭 𝓑𝓮𝔂𝓸𝓷𝓭 𝓦𝓸𝓻𝓭𝓼✮⋆˙")
    st.subheader("✰⋆⁺₊⋆𝓛𝓮𝓽’𝓼 𝓭𝓲𝓿𝓮 𝓲𝓷𝓽𝓸 𝓽𝓱𝓮 𝓳𝓸𝔂!⋆⁺₊⋆✰")
    with st.spinner("Generating Please wait........."):
        result=chain.run({"story":story,"input_text":text,"Genre":Genre,"language":language})
        st.write(result)
        
       



    promt_sum=PromptTemplate(input_variables=["input_text"], 
        template="Translate the provided {input_text} into English, and summarize it in onto a meaningfull sentence of 10 words.")
    chain_sum=promt_sum|llm|parser
    summarized_text=chain_sum.invoke({"input_text":result})


    # Define the text prompt
    summerized_prompt = summarized_text
    # Check the length of the summarized text and trim if necessary
    max_prompt_length = 1000
    if len(summarized_text) > max_prompt_length:
        summarized_text = summarized_text[:max_prompt_length]
        print(f"Truncated summarized text to fit within the limit of {max_prompt_length} characters.")
    
    print(f"we created Summarized text: {summarized_text}")
    try:
        response = openai.Image.create(
            prompt=summerized_prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']

        print(f"Image generated successfully: {image_url}")

        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        
        st.image(img)
        st.button("let's hear",on_click=speaking,args=(str(result),img,))


    except Exception as e:
        print(f"An error occurred while generating the image: {e}")



    

with st.sidebar:
    text=st.text_input("Which narrative would you like to explore?")
    #text={"input_text":input}
    st.button("Let’s hit the road!😊✨", on_click=on_button_click)

def speaking(result,img):
     # Create gTTS object
        print(f"********************printing the result{result}")
        gtts_languages = {"Afrikaans": "af", "Arabic": "ar", "Bulgarian": "bg", "Bengali": "bn", "Bosnian": "bs", "Catalan": "ca", "Czech": "cs", "Welsh": "cy", "Danish": "da", "German": "de", "Greek": "el", "English": "en", "Esperanto": "eo", "Spanish": "es", "Estonian": "et", "Finnish": "fi", "French": "fr", "Gujarati": "gu", "Hebrew": "he", "Hindi": "hi", "Croatian": "hr", "Hungarian": "hu", "Indonesian": "id", "Icelandic": "is", "Italian": "it", "Japanese": "ja", "Javanese": "jw", "Kannada": "kn", "Khmer": "km", "Korean": "ko", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Malayalam": "ml", "Marathi": "mr", "Malay": "ms", "Myanmar (Burmese)": "my", "Nepali": "ne", "Dutch": "nl", "Norwegian": "no", "Polish": "pl", "Portuguese (Brazil)": "pt", "Portuguese (Portugal)": "pt", "Romanian": "ro", "Russian": "ru", "Sinhala": "si", "Slovak": "sk", "Albanian": "sq", "Serbian": "sr", "Sundanese": "su", "Swedish": "sv", "Swahili": "sw", "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Ukrainian": "uk", "Urdu": "ur", "Vietnamese": "vi", "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW", "Zulu": "zu"}
        tts = gTTS(text=result, lang=gtts_languages[language], slow=False)
        # Save the speech to a file
        timestamp = int(time.time())
        filename = f"output_{timestamp}.mp3"
        tts.save(filename)
        st.write(result)
        st.image(img)

        st.audio(filename, format="audio/mp3")
