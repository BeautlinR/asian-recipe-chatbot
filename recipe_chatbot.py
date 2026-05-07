import streamlit as st
import pyttsx3
import speech_recognition as sr

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_speech" not in st.session_state:
    st.session_state.pending_speech = None

if "last_input" not in st.session_state:
    st.session_state.last_input = ""

def speak(text):
  engine = pyttsx3.init()
  engine.setProperty('rate', 150)
  engine.say(text)
  engine.runAndWait()
  engine.stop()


def chatbot_response(query):
    query = query.lower().strip()
    if not query: return ""

    if "hello" in query or "hey" in query:
        return "Hello!"

    elif "who are you" in query:
      return "I am your Asian Recipe Bot!\nTell me what ingredient do you have?\nChoose anyone of these chicken, rice, noodles, eggs, tofus, prawn, paneer, dumpling"

    elif "bye" in query or "stop" in query:
        return "Thank you! Happy Cooking! Goodbye!"

    elif "chicken" in query:
        return "you can make biryani or thai curry.\nChoose any one"
    elif "biryani" in query:
        return "step 1. Marinate chicken in yogurt and biryani spices for 2 hours \n Step 2. Fry onions till golden brown and keep aside \n Step 3. Cook marinated chicken in a pot till half done \n Step 4. Parboil basmati rice separately \n Step 5. Layer rice over chicken in pot \n Step 6. Add saffron milk and fried onions on top \n Step 7. Seal pot and cook on low flame for 25 minutes \n Step 8. Mix gently and serve with raita"
    elif "thai curry" in query:
        return "step 1. Heat oil and fry green curry paste for 2 minutes \n Step 2. Add chicken pieces and cook till white \n Step 3. Pour in coconut milk and stir well \n Step 4. Add vegetables like eggplant and zucchini \n Step 5. Simmer for 20 minutes \n Step 6. Add fish sauce and sugar to balance taste \n Step 7. Garnish with basil and serve with jasmine rice"

    elif "rice" in query:
        return "You can make fried or sushi.\nChoose any one"
    elif "fried" in query:
        return "Step 1. Cook rice and spread on a tray to cool completely \n Step 2. Heat oil in a wok on high flame \n Step 3. Add garlic and fry for 30 seconds \n Step 4. Add vegetables and stir fry for 3 minutes \n Step 5. Push everything to the side and scramble eggs \n Step 6. Mix in the cold rice and stir fry for 5 minutes \n Step 7. Add soy sauce and sesame oil and toss well \n Step 8. Serve hot with chilli sauce"
    elif "sushi" in query:
        return "Step 1. Wash rice until water runs clear \n Step 2. Cook rice in rice cooker or pot with water \n Step 3. Mix rice vinegar sugar and salt in a bowl \n Step 4. Pour vinegar mixture over hot cooked rice \n Step 5. Fold gently with a wooden spoon do not mash \n Step 6. Fan the rice while folding to cool it down \n Step 7. Use immediately for sushi rolls"

    elif "noodles" in query:
        return "You can make pad thai, ramen or hakka.\nChoose any one"
    elif "pad thai" in query:
        return "Step 1. Soak rice noodles in warm water for 30 minutes \n Step 2. Mix tamarind paste fish sauce and sugar for sauce \n Step 3. Heat oil in wok and fry garlic and tofu \n Step 4. Add shrimp and cook for 2 minutes \n Step 5. Add drained noodles and pour sauce over them \n Step 6. Push to the side and scramble eggs \n Step 7. Add bean sprouts and mix everything \n Step 8. Top with crushed peanuts lime and chilli"
    elif "ramen" in query:
        return "Step 1. Boil pork bones for 2 hours to make rich broth \n Step 2. Add soy sauce and mirin to the broth \n Step 3. Cook ramen noodles separately as per packet \n Step 4. Soft boil eggs for 6 minutes and peel \n Step 5. Slice chashu pork thinly \n Step 6. Place noodles in a bowl and pour hot broth \n Step 7. Top with pork slices egg nori and spring onions"
    elif "hakka" in query:
        return "Step 1. Boil hakka noodles with salt and oil until al dente \n Step 2. Drain and rinse with cold water to stop cooking \n Step 3. Heat oil in wok and fry garlic for 30 seconds \n Step 4. Add capsicum cabbage and carrot and stir fry \n Step 5. Add noodles and toss on high flame \n Step 6. Add soy sauce vinegar and chilli sauce \n Step 7. Toss well for 3 minutes and serve hot"

    elif "eggs" in query:
        return "You can make tamagoyaki or korean steamed egg.\nChoose any one"
    elif "tamagoyaki" in query:
        return "Step 1. Beat 3 eggs with soy sauce mirin and sugar \n Step 2. Heat a rectangular pan and oil lightly \n Step 3. Pour a thin layer of egg and let it set partially \n Step 4. Roll the egg to one end of the pan \n Step 5. Add another layer of egg mixture and roll again \n Step 6. Repeat 3 to 4 times to build layers \n Step 7. Remove and shape with a sushi mat \n Step 8. Slice and serve with soy sauce"
    elif "korean steamed egg" in query:
        return "Step 1. Beat 3 eggs well in a bowl \n Step 2. Add warm anchovy broth and salt and mix \n Step 3. Pour into a stone pot or bowl \n Step 4. Steam on low heat with lid on for 12 minutes \n Step 5. The egg should be soft and jiggly \n Step 6. Garnish with chopped spring onion and sesame oil \n Step 7. Serve immediately while hot"

    elif "tofus" in query:
        return "You can make mapo or agedashi.\nChoose any one"
    elif "mapo" in query:
        return "Step 1. Cut soft tofu into cubes carefully \n Step 2. Fry minced pork in oil until browned \n Step 3. Add doubanjiang paste and fry for 1 minute \n Step 4. Add chicken broth and bring to boil \n Step 5. Gently add tofu cubes and simmer for 5 minutes \n Step 6. Mix cornstarch with water and pour in to thicken \n Step 7. Finish with Sichuan pepper and spring onions"
    elif "agedashi" in query:
        return "Step 1. Drain silken tofu and pat completely dry \n Step 2. Cut into cubes and coat with cornstarch \n Step 3. Deep fry in hot oil until light golden \n Step 4. Make broth with dashi soy sauce and mirin \n Step 5. Heat broth gently in a small pot \n Step 6. Place fried tofu in a bowl and pour warm broth \n Step 7. Top with grated daikon ginger and bonito flakes"

    elif "prawn" in query:
        return "You can make butter garlic or thai curry.\nChoose any one"
    elif "butter garlic" in query:
        return "Step 1. Clean and devein prawns and pat dry \n Step 2. Melt butter in a pan over medium heat \n Step 3. Add finely chopped garlic and fry for 1 minute \n Step 4. Add prawns and cook for 2 minutes each side \n Step 5. Add chilli flakes and lemon juice \n Step 6. Toss well and cook for 1 more minute \n Step 7. Garnish with parsley and serve with bread"
    elif "thai curry" in query:
        return "Step 1. Heat oil and fry red curry paste for 2 minutes \n Step 2. Add lemongrass and kaffir lime leaves \n Step 3. Pour in coconut milk and stir to combine \n Step 4. Add prawns and cook for 4 minutes only \n Step 5. Add fish sauce and palm sugar to taste \n Step 6. Add cherry tomatoes and cook 2 more minutes \n Step 7. Serve over jasmine rice with fresh basil"

    elif "paneer" in query:
        return "You can make butter masala, palak or tikka.\nChoose any one"
    elif "butter masala" in query:
        return "Step 1. Fry paneer cubes in butter until lightly golden \n Step 2. In same pan fry onions until soft \n Step 3. Add ginger garlic paste and cook 2 minutes \n Step 4. Add tomato puree and all spices \n Step 5. Cook masala for 10 minutes till oil separates \n Step 6. Add water and bring to a boil \n Step 7. Add fried paneer and simmer for 10 minutes \n Step 8. Stir in cream and kasuri methi and serve"
    elif "palak" in query:
        return "Step 1. Blanch spinach in boiling water for 2 minutes \n Step 2. Cool and blend into smooth puree \n Step 3. Fry onion garlic and ginger in oil \n Step 4. Add spices and cook for 2 minutes \n Step 5. Add spinach puree and mix well \n Step 6. Simmer for 10 minutes on low flame \n Step 7. Add paneer cubes and cook 5 more minutes \n Step 8. Finish with cream and serve with roti"
    elif "tikka" in query:
        return "Step 1. Cut paneer into thick cubes \n Step 2. Mix yogurt with tandoori masala and spices \n Step 3. Marinate paneer in yogurt mixture for 2 hours \n Step 4. Thread paneer capsicum and onion on skewers \n Step 5. Grill in oven at 200 degrees for 15 minutes \n Step 6. Baste with butter midway through grilling \n Step 7. Serve with mint chutney and lemon"

    elif "dumpling" in query:
        return "You can make steamed momos or japanese gyoza.\nChoose any one"
    elif "steamed momos" in query:
        return "Step 1. Make dough with flour and water and rest 30 minutes \n Step 2. Mix minced chicken with ginger garlic onion and spices \n Step 3. Roll dough into small thin circles \n Step 4. Place filling in centre and pleat edges to seal \n Step 5. Steam in a steamer for 12 minutes \n Step 6. Make chutney with tomato and chilli \n Step 7. Serve hot with spicy chutney"
    elif "japanese gyoza" in query:
        return "Step 1. Mix pork mince with cabbage ginger garlic and soy \n Step 2. Place filling on gyoza wrapper and fold and pleat \n Step 3. Heat oil in a flat pan over medium heat \n Step 4. Place gyoza flat side down and fry 2 minutes \n Step 5. Add water and cover with lid immediately \n Step 6. Steam for 5 minutes until water evaporates \n Step 7. Serve with soy sauce and rice vinegar dip"

    elif "thanks" in query:
        return "You are welcome! Happy cooking!"
    else:
       return "I didn’t understand. Try again."

st.set_page_config(page_title= "Asian Recipe Chatbot", layout= "centered")

st.markdown(
    """
    <style>
    .stApp {
       background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    }
    h1{
       text-align: center;
       color: #2D3436; font-family: 'Helvetica';
       }
    .user-msg{
       background-color: #FFA400;
       color: white;
       padding: 10px 15px;
       border-radius: 18px 18px 18px 0px;
       max-width: 65%;          /* BUBBLE WIDTH FIXED */
       width: fit-content;      /* SHRINKS TO TEXT SIZE */
       margin-left: auto;       /* PUSHES TO RIGHT */
       text-align: left;
       word-wrap: break-word;
       align-self: flex-end;     
       }
    .bot-msg{
       background-color: #FFFFFF;;
       color: #2D3436; 
       padding: 10px 15px;
       border-radius: 18px 18px 18px 0px;
       max-width: 65%;          /* BUBBLE WIDTH FIXED */
       width: fit-content;      /* SHRINKS TO TEXT SIZE */
       margin-right: auto;      /* STAYS ON LEFT */
       text-align: left;
       word-wrap: break-word;
       white-space: pre-line;
       align-self: flex-start;
        }
    .chat-box {
    max-height: 500px;
    overflow-y: auto;
    padding: 10px; 
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);   
    }
    .col1,.col2,.col3{
    border: 2px solid;
    border-radius: 15px;
    padding: 15px;
    height: 450px;
    overflow-y: auto;
    background-color: #FFFDF7;
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🍽️Asian Recipe Chatbot🥘</h1>", unsafe_allow_html=True)

chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        div_class = "user-msg" if msg["role"] == "user" else "bot-msg"
        st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

def send_message():
    user_input = st.session_state.input_text.strip()

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        reply = chatbot_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": reply})
        st.session_state.pending_speech = reply
        st.session_state.input_text = ""

def clear_chat():
    st.session_state.messages = []
    st.session_state.pending_speech = None
    st.session_state.last_input=""

st.text_input("Type your message", key="input_text",on_change=send_message,placeholder="e.g. chicken, biryani, ramen...")

col1, col2, col3 = st.columns(3)


with col1:
    st.button("Send", on_click=send_message,use_container_width=True)
with col3:
     st.button("Clear",on_click=clear_chat,use_container_width=True)
with col2:
    if st.button("🎙️Speak",use_container_width=True):
        r = sr.Recognizer()
        with sr.Microphone() as source:
           st.toast("Listening...")

           try:
             audio = r.listen(source, timeout=5, phrase_time_limit=5)
             text = r.recognize_google(audio)
             st.session_state.messages.append({"role": "user", "content": text})
             reply = chatbot_response(text)
             st.session_state.messages.append({"role": "bot", "content": reply})
             st.session_state.pending_speech = reply
             st.rerun()
           except:
             st.error("Can't hear you!")

if st.session_state.pending_speech:
    speech_text = st.session_state.pending_speech
    st.session_state.pending_speech = None
    speak(speech_text)

