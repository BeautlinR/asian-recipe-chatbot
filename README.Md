# 🍽️ Asian Recipe Chatbot

A voice-enabled, interactive recipe assistant built with **Streamlit** that guides you through Asian recipes step by step — using either text or your microphone.
***
### **✨ Features**
<!-- TOC -->
* **💬 Text Chat —** Type an ingredient or dish name to get a recipe

* **🎙️ Voice Input —** Speak your query using the microphone button
 
* **🔊 Text-to-Speech —** The bot reads recipe steps aloud
 
* **🧹 Clear Chat —** Reset the conversation at any time

* **🌏 10+ Asian Cuisines —** Covers Indian, Japanese, Korean, Thai, Chinese, and more
<!-- TOC -->
***
### **🥘 Supported Ingredients & Dishes**

   | **Ingredient** | **Available Dishes**           |                                  
   | Chicken        | Biryani,Thai Curry             |  
   |  Rice          | Fried Rice,Sushi               |  
   |  Noodles       | Pad Thai,Ramen,Hakka           |  
   |  Eggs          | Tamagoyaki,Korean steamed Egg  |  
   |  Tofu          | MapoTofu,Agedashi Tofu         |  
   |  Prawn         | Butter Garlic Prawn,Thai Curry |  
   |  Paneer        | Butter Masala,Palak,Tikka      |  
   |  Dumpling      | SteamedMomos,Japanese Gyoza    |  
***
### **🗂️ Project Structure**
            
asian-recipe-chatbot/
│
├── recipe_chatbot.py   # Main application file 
├── requirements.txt    # Python dependencies 
└── README.md           # Project documentation
***
### **⚙️Requirements**
<!-- TOC -->
* Python **3.8 or higher**

* A working **microphone**(for voice input)

* Internet connection(for Google Speech Recognition)
<!-- TOC -->
***
### **🚀 Installation & Setup**
**Step 1 — Clone or Download the Project**
   
git clone https://github.com/BeautlinR/asian-recipe-chatbot cd asian-recipe-chatbot 
 
 Or simply place recipe_chatbot.py and requirements.txt in the same folder.
***

**Step 2 — Create a Virtual Environment (Recommended)**

python -m venv venv 

Activate it:                                            
 * **Windows:** venv\Scripts\activate
 * **macOS/Linux:** source venv/bin/activate
***
**Step 3 — Install Dependencies**

pip install -r requirements.txt 

**⚠️ PyAudio Note:** PyAudio requires system-level audio libraries. If pip install fails:

**Windows:** pip install pipwin then pipwin install pyaudio

**macOS:**  brew install portaudio then pip install pyaudio

**Linux (Ubuntu/Debian):** sudo apt-get install portaudio19-dev then pip install pyaudio
***
**Step 4 — Run the Application**

streamlit run recipe_chatbot.py 

The app will automatically open in your browser at http://localhost:8501.
***
### **💡How to Use**

 1. **Start the app** using the command above.

 2. **Type** an ingredient (e.g., chicken) in the text box and press **Enter** or click **Send.**

 3. The bot will suggest dishes — type the dish name to get the full recipe.

 4. Click **🎙️ Speak** to use your voice instead of typing.

 5. The bot will also **read the recipe aloud** via text-to-speech.

 6. Click **Clear** to reset the conversation anytime.

**Example Conversation**

You → chicken

Bot → You can make biryani or thai curry. Choose any one.

You → biryani

Bot → Step 1. Marinate chicken in yogurt and biryani spices... 
***

### **🛠️ Troubleshooting**
 
|**Problem**                  |**Solution**                                             |
|Microphone not working       |Check browser/OS microphone permissions                     |
|PyAudio install fails        |Follow the OS-specific install steps in Step 3              |
|No sound from text-to-speech |Ensure your system audio/speakers are on                    |
|streamlit: command not found |Make sure your virtual environment is activated             |
|Speech not recognised        |Speak clearly; ensure you have a stable internet connection |

***
### **📦 Dependencies**

 
|**Package**       |**Purpose**                                |
|streamlit         | Web UI framework                          |
|pyttsx3           | Offline text-to-speech engine             |
|SpeechRecognition | Converts microphone audio to text         |
|PyAudio           | Audio stream interface for the microphone |


***