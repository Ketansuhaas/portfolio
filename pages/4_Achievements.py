import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Achievements"
)

st.title("Achievements")
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

c1, c2 ,c3, c4= st.container(), st.container(), st.container(), st.container()

c1.header("International Collegiate Programming Contest (ICPC) - 2020")
c1.markdown('<p class="big-font"><i>Secured an All India Rank of 379 at the Asia Amritapuri Double-site Regional Contest. It is an international-level competitive programming contest between colleges.</i></p>', unsafe_allow_html=True)

c3.header("Kishore Vaigyanik Protsahan Yojana (KVPY) Scholar - 2018")
c3.markdown('<p class="big-font"><i>Cleared the KVPY exam and secured an All India Rank of 1237 in the SX Stream, which is for 12th-grade students. It is also the admission exam for the prestigious Indian Institute of Science and fellowship.</i></p>', unsafe_allow_html=True)

c4.header("Indian National Physics Olympiad (INPhO) - 2018")
c4.markdown('<p class="big-font"><i>Participated after clearing the National Standard Examination in Physics (NSEP) securing a place amongst the top 17 in Tamil Nadu State. INPhO has to be cleared for participating in the International Physics Olympiad (IPhO).</i></p>', unsafe_allow_html=True)

c2.header("Joint Entrance Examination (JEE) Advanced - 2019")
c2.markdown('<p class="big-font"><i>Secured an All India Rank of 1640 out of around 1,200,000 candidates from JEE Main, where I secured a rank of 1390. This is the admission exam to the Indian Institute of Technologies (IITs).</i></p>', unsafe_allow_html=True)
