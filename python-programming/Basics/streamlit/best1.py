import streamlit as st
import time
st.title("hello stream lit")
st.header("Text Elements")
st.subheader("Subheader Example")
st.text("This is a simple text block.")
st.markdown("This is **Markdown** text.")
st.caption("This is a caption.")
st.json({"name": "Streamlit", "version": "1.0"})
st.checkbox("Show Message")
st.radio("Pick a genre:", ['Comedy', 'Drama', 'Documentary'])
st.selectbox("Choose a number:", [1, 2, 3, 4, 5])
st.text_input("Enter your name:", "Streamlit User")
st.text_area("Tell us about yourself:", "Write here...")
st.number_input("Pick a number:", 0, 100)
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.write(f"Uploaded File Name: {uploaded_file.name}")
st.date_input("Pick a date:")
st.time_input("Pick a time:")
st.color_picker("Pick a color:", "#00f900")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content in Tab 1")
with tab2:
    st.write("Content in Tab 2")
st.header("Media")
st.image("https://placekitten.com/400/300", caption="Cute Kitten", use_column_width=True)
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
# progress_bar = st.progress(0)
# for i in range(100):
#     time.sleep(0.5)
#     progress_bar.progress(i + 1)   
st.header("Caching")
@st.cache_data
def expensive_computation(a, b):
    time.sleep(2)  # Simulate computation
    return a + b

result = expensive_computation(5, 3)
st.write("Cached Result:", result)  
st.sidebar.title("Sidebar Example")
st.sidebar.radio("Navigation", ['Home', 'About'])
st.sidebar.slider("Sidebar Slider", 0, 50)  

if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")

if st.button("Increment"):
    st.session_state.counter += 1

if "input_text" not in st.session_state:
    st.session_state.input_text = ""


def clear_text():
    st.session_state["input_text"] = ""  # Clear the session state

# Input box with key binding to session state
text=st.text_input("Type something:", key="input_text")

# Button to clear the text
if st.button("Clear Text"):
    clear_text()
    st.write(text)
