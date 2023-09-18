import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Education"
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

st.title("Education")
c1, c2 = st.container(), st.container()
c1c1,c1c2 = c1.columns(2)
c2c1,c2c2 = c2.columns(2)

c1c2.image("BU.png",width=180)
c1c1.markdown('<p class="head-font"><b>Boston University</b></p>', unsafe_allow_html=True)

c1c1.markdown('<p class="big-font">Masters in Artificial Intelligence (2023 - Present)</p>', unsafe_allow_html=True)




c2c2.image("IITR.png", width=180)
c2c1.markdown('<p class="head-font"><b>Indian Institute of Technology (IIT) Roorkee</b></p>', unsafe_allow_html=True)
c2c1.markdown('<p class="big-font">Bachelor of Technology in Electrical Engineering (2019 - 2023)<br>CGPA : 8.645/10</p>', unsafe_allow_html=True)
