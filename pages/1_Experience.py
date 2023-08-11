import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Experience"
)
st.title("Experience")

c1, c2 = st.container(), st.container()
c1c1,c1c2 = c1.columns(2)
c2c1,c2c2 = c2.columns(2)

c1c2.image("slice.png",width=400)
c1c1.header("Slice")
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)
c1c1.markdown('<p class="big-font"><i>Software Development Intern (May 2022 - July 2022)</i> <ul><li>Worked as a backend engineer in the payment gateway service team.</li><li>Created APIs and integrated Juspay endpoints for customer order creation and order status retrieval using Springboot in Java.</li><li>Suggested efficient changes to the backend and helped enhance the fraudulent detection system using machine learning methods.</li></p>', unsafe_allow_html=True)



c2c2.image("IITR.png", width=180)
c2c1.header("Machine Learning Lab, Electrical Engineering Dept, IITR")
c2c1.markdown('<p class="big-font"><i>Research Apprentice (August 2022 - May 2023)</i> <ul><li>Collaborated with a Ph.D. student and explored the area of semantic segmentation for biomedical images.<li>Discussed the nn-U-Net architecture in detail and verified its benchmarks by training.</li></p>', unsafe_allow_html=True)

