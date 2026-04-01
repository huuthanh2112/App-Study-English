import streamlit as st
from deep_translator import GoogleTranslator
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

translator = Translator()

def get_word_type(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return "Không rõ"

    pos = synsets[0].pos()

    return {
        'n': 'Danh từ',
        'v': 'Động từ',
        'a': 'Tính từ',
        'r': 'Trạng từ'
    }.get(pos, "Khác")

def translate(text, dest='vi'):
    try:
        return GoogleTranslator(source='auto', target=dest).translate(text)
    except:
        return "Lỗi dịch 😢"

st.title("📚 App học từ vựng tiếng Anh")

tab1, tab2 = st.tabs(["Học từ vựng", "Chatbot"])

with tab1:
    word = st.text_input("Nhập từ tiếng Anh:")

    if word:
        meaning = translate(word, 'vi')
        word_type = get_word_type(word)

        st.write(f"👉 Nghĩa: {meaning}")
        st.write(f"👉 Loại từ: {word_type}")

with tab2:
    user_input = st.text_input("Bạn muốn hỏi gì?")

    if user_input:
        if "nghĩa" in user_input or "dịch" in user_input:
            word = user_input.split()[-1]
            meaning = translate(word, 'vi')
            st.write(f"👉 {word} = {meaning}")
        else:
            st.write("🤖 Mình chưa hiểu câu này 😅")
