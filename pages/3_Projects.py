import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Projects"
)
c1, c2 ,c3 ,c4, c5 = st.container(), st.container() , st.container(), st.container(), st.container()
#c1c2.image("Slice.png",width=400)
c1.title("Cardiac Image Segmentation using Deep Learning")
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)
c1.markdown('<p class="big-font"><i>(August 2022-May 2023)</i> <ul><li>Implemented some U-Net-based attention models in Tensorflow for the semantic segmentation of Cardiac MRI Images.</li><li>Achieved a significantly good dice coefficient on the M&Ms Dataset.</li><li>Designed a web application using the Streamlit framework in Python.</li></p>', unsafe_allow_html=True)
c1.write("GitHub repository is [here.](https://github.com/Ketansuhaas/cardiac-image-segmentation)")
c1.write("Project report is [here.](https://github.com/Ketansuhaas/cardiac-image-segmentation/blob/main/Final%20BTP%20report%20for%20masters.pdf)")


c2.title("arXiv Research Article Recommender")
c2.markdown('<p class="big-font"><i>(August 2023-Present)</i> <ul><li> Utilized BERT embeddings for encoding the titles of a portion of the arXiv dataset. </li><li>Using abstracts instead of titles would produce better results, but will require a higher computational power. </li><li>Trained a K-Means model to recommend related research articles.</li><li>Designed and deployed an elegant web application in Streamlit.</li></p>', unsafe_allow_html=True)
c2.write("GitHub repository is [here.](https://github.com/Ketansuhaas/arXiv-article-recommender)")
c2.write("Access the web-app [here.](https://arxiv-article-recommender-8uq7kkdrefhdsf8m5xkge7.streamlit.app/)")


c3.title("Next Word Predictor")
c3.markdown('<p class="big-font"><i>(May 2023-August 2023)</i> <ul><li>Implemented a stacked LSTM model in Keras for predicting the next possible words of a sentence.</li><li>Designed an elegant multipage web application using Streamlit that also allows training the model on a context text before prediction.</li><li>Displays the probability of all the words that could appear next.</li></p>', unsafe_allow_html=True)
c3.write("GitHub repository is [here.](https://github.com/Ketansuhaas/next-word-predictor)")


c4.title("Hand-gesture-controlled mouse using Computer Vision")
c4.markdown('<p class="big-font"><i>(October 2022-November 2022)</i> <ul><li>Created an end-to-end desktop AI mouse app using OpenCV, utilizing the media pipe library to detect hands. </li><li>Designed algorithms for detecting physical hand gestures for moving and clicking the mouse pointer of the PC.</li></p>', unsafe_allow_html=True)
c4.write("GitHub repository is [here.](https://github.com/Ketansuhaas/AIMouse)")


c5.title("Solving Economic Load Dispatch Problem On Quantum Computers   ")
c5.markdown('<p class="big-font"><i>(January 2022-March 2022)</i> <ul><li>Economic Load Dispatch involves the optimal allocation of generation units across all generators, satisfying the power, voltage, transmission line, and network security constraints.</li><li>Used the LeapCQM Quantum Annealing-based hybrid solver on the D-Wave Leap IDE in Python for computation.</li><li>Successfully reduced the time of computation significantly (in the range of 10^3 sec) for solving the economic load dispatch problem, proving the efficacy of quantum computers over classical ones.</li></p>', unsafe_allow_html=True)
c5.write("Project report is [here.](https://drive.google.com/file/d/1d3f8KkhOTx2XdEwzirhHxv2sQE_z9cuh/view?usp=sharing)")