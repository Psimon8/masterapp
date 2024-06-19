import streamlit as st
import subprocess

st.set_page_config(
    layout="wide",
    page_title="Similarity Refine",
    page_icon="🥥"
)

def run_app1():
    try:
        result = subprocess.run(["streamlit", "run", "apps/keyword-refine/keyword-app.py"], capture_output=True, text=True, check=True)
        st.write(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to run Keyword Refine: {e.stderr}")

def run_app2():
    try:
        result = subprocess.run(["streamlit", "run", "apps/similarity-refine/similarity-app.py"], capture_output=True, text=True, check=True)
        st.write(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to run Similarity Refine: {e.stderr}")

def run_app3():
    try:
        result = subprocess.run(["streamlit", "run", "app3/app.py"], capture_output=True, text=True, check=True)
        st.write(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to run App 3: {e.stderr}")

st.sidebar.title("Navigation")
app = st.sidebar.radio("Go to", ["Keyword Refine", "App 2", "App 3"])

if app == "Keyword Refine":
    st.title("Keyword Refine")
    run_app1()
elif app == "App 2":
    st.title("App 2")
    run_app2()
elif app == "App 3":
    st.title("App 3")
    run_app3()
