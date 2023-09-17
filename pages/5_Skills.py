import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Skills"
)
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Technical Skills")

#st.header('''Programming languages: Python, C++, MATLAB, Java''')
#st.header("Developer Tools: PyCharm, Jupyter Notebook, Visual Studio Code, Anaconda, Github, Linux terminal, Postman, Command prompt, IntelliJ IDEA")
#st.header("Technologies/Frameworks: NumPy, Pandas, Keras, TensorFlow, PyTorch, Scikit-learn, Matplotlib, OpenCV, Springboot, JUnit/Mockito, Simulink")
st.markdown('<p class="big-font">\
        <h5><b>PROGRAMMING LANGUAGES : </b>C++, Python, Java, MATLAB</h5>\
        <h5><b>TOOLS AND SOFTWARE : </b>Visual Studio Code, PyCharm, Jupyter Notebook, Anaconda, GitHub, Git, Terminal,Postman, IntelliJ IDEA, Linux</h5>\
        <h5><b>FRAMEWORKS: </b>Keras, TensorFlow, PyTorch, Langchain, Scikit-learn, Matplotlib, OpenCV, Numpy, Pandas,Spring Boot, JUnit/Mockito</h5></p>', unsafe_allow_html=True)
