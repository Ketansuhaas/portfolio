import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Projects"
)
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
.head-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)
st.title("Projects")
c1, c2 ,c3 ,c4, c5 = st.container(), st.container() , st.container(), st.container(), st.container()
#c1c2.image("Slice.png",width=400)
c1.header("Cardiac MRI Image Segmentation using Deep Learning")
c1.image("cis.jpg")

c1.markdown('<p class="big-font">(August 2022 - May 2023) <ul>\
            <li>Implemented advanced U-Net-based attention models in TensorFlow for the semantic segmentation of 3D Cardiac short-axis MRI Images.</li>\
            <li>Conducted a thorough comparison of model results and recorded performance benchmarks.</li>\
            <li>Achieved a significantly high dice coefficient on the M&Ms Dataset.</li>\
            <li>Designed an interactive web application using Streamlit framework in Python.</li></ul></p>', unsafe_allow_html=True)
c1.write("GitHub repository is [here.](https://github.com/Ketansuhaas/cardiac-image-segmentation)")
c1.write("Pre-print is [here.](https://github.com/Ketansuhaas/cardiac-image-segmentation/blob/main/Final%20BTP%20report%20for%20masters.pdf)")


c2.header("arXiv Research Article Recommender")
c2.image("ar.jpg")
c2.markdown('<p class="big-font">(August 2023 - Present) <ul>\
            <li>Leveraged BERT embeddings to encode titles from a subset of the arXiv dataset.</li>\
            <li>Currently working on utilizing abstracts for improved results, albeit with higher computational demands.</li>\
            <li>Developed a K-Means model for recommending related research articles.</li><li>Designed and deployed an elegant web application using Streamlit.</li></ul></p>', unsafe_allow_html=True)
c2.write("GitHub repository is [here.](https://github.com/Ketansuhaas/arXiv-article-recommender)")
c2.write("Access the web-app [here.](https://arxiv-article-recommender-8uq7kkdrefhdsf8m5xkge7.streamlit.app/)")


c3.header("Next Word Predictor")
c31,c32 = c3.columns(2)
c31.image("nw1.jpg")
c32.image("nw2.jpg")
c3.markdown('<p class="big-font">(May 2023 - August 2023)<ul>\
            <li>Implemented a stacked LSTM model in Keras for predicting the next possible words of a sentence.</li>\
            <li>Designed an elegant multipage web application using Streamlit.</li>\
            <li>Allows training the model on a context text before prediction.</li>\
            <li>Displays the probability of all the words that could appear next.</li></ul></p>', unsafe_allow_html=True)
c3.write("GitHub repository is [here.](https://github.com/Ketansuhaas/next-word-predictor)")


c4.header("Hand-gesture-controlled mouse using Computer Vision")
c4.image("Aimouse.jpg")
c4.markdown('<p class="big-font">(October 2022 - November 2022) <ul>\
            <li>Developed an end-to-end desktop AI mouse application using the Pyinstaller library.</li>\
            <li>Leveraged the MediaPipe library for precise finger coordinate detection and devised algorithms for recognizing physical hand gestures.</li>\
            <li>Incorporated the AutoPy library for intuitive mouse pointer control.</li></ul></p>', unsafe_allow_html=True)
c4.write("GitHub repository is [here.](https://github.com/Ketansuhaas/AIMouse)")


c5.header("Solving Economic Load Dispatch Problem On Quantum Computers   ")
c5.markdown('<p class="big-font">(January 2022 - March 2022) <ul>\
            <li>Economic Load Dispatch involves the optimal allocation of generation \
            units across all generators, satisfying the power, voltage, transmission line,\
             and network security constraints.</li>\
            <li>Used the LeapCQM Quantum Annealing-based hybrid \
            solver on the D-Wave Leap IDE in Python for computation.</li>\
            <li>Successfully reduced the time of computation significantly \
            (in the range of 10^3 sec) for solving the economic load dispatch problem, \
            proving the efficacy of quantum computers over classical ones.</li></ul></p>', unsafe_allow_html=True)
c5.write("Project report is [here.](https://drive.google.com/file/d/1d3f8KkhOTx2XdEwzirhHxv2sQE_z9cuh/view?usp=sharing)")