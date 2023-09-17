import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Achievements"
)

st.title("Achievements")
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

c1, c2 ,c3, c4= st.container(), st.container(), st.container(), st.container()

c1.markdown('<p class="head-font"><b>International Collegiate Programming Contest (ICPC) - 2020</b></p>', unsafe_allow_html=True)
c1.markdown('<p class="big-font">Secured an All India Rank of 379 at the Asia Amritapuri Double-site Regional Contest. \
            It is an international competitive programming contest between institutions.</p>', unsafe_allow_html=True)

c2.markdown('<p class="head-font"><b>Kishore Vaigyanik Protsahan Yojana (KVPY) Scholar - 2018</b></p>', unsafe_allow_html=True)
c2.markdown('<p class="big-font">Cleared the KVPY exam and secured an All India Rank of 1237 in the SX Stream, \
            which is for 12th-grade students. \
            It is the admission exam for the prestigious Indian Institute of Science and also for the fellowship.</p>', unsafe_allow_html=True)

c3.markdown('<p class="head-font"><b>Indian National Physics Olympiad (INPhO) - 2018</b></p>', unsafe_allow_html=True)
c3.markdown('<p class="big-font">Participated after clearing the National Standard Examination in Physics \
            (NSEP) securing a place amongst the top 17 in Tamil Nadu State. \
            INPhO has to be cleared for participating in the International Physics Olympiad (IPhO).</p>', unsafe_allow_html=True)

c4.markdown('<p class="head-font"><b>Joint Entrance Examination (JEE) Advanced - 2019</b></p>', unsafe_allow_html=True)
c4.markdown('<p class="big-font">Secured an All India Rank of 1640 out of around 1,200,000 candidates from JEE Main, \
            in which I secured a rank of 1390. This is the admission exam to the Indian Institute of Technologies (IITs).</p>', unsafe_allow_html=True)
