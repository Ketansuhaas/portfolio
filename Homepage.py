import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Portfolio"
)
st.title("Ketan Suhaas Saichandran")
c1,c2 = st.columns(2)
c1.write('''Greetings, I am an AI graduate student at **Boston University** with a diverse academic background from the **Indian Institute of Technology (IIT) Roorkee**, where I majored in Electrical Engineering.
My insatiable curiosity has led me to explore a wide array of domains. In my first year of bachelor's, I leaped into my first hackathon, where, I created a virtual operating system in Python just two days after learning the language. This achievement fueled my drive for challenges.\n
Competitive programming became my forte throughout my undergraduate years, culminating in success at prestigious contests like ICPC. I delved into cybersecurity, mastered Kali Linux, and delved into mathematical cryptography under a respected professor's guidance from IIT Kharagpur.
Data structures, algorithms, and the synergy between graph algorithms and computer vision captivated me. Notably, I crafted a creative project – an image-maze solver using the BFS algorithm.\n
My journey into machine learning and data science began early, evolving into a profound interest in deep learning after a comprehensive course during my final year. The pinnacle of my undergraduate journey was a Bachelor's project in deep learning, focusing on the semantic segmentation of cardiac MRI images. This project illuminated the beauty and potential of deep learning, setting the stage for further exploration.
Nurturing my deep learning fascination, I dived into Natural Language Processing and pursued independent projects. Currently, I also started exploring the exciting field of Generative AI.\n
Research has always been my thing since I was a kid. Always driven by intuition. Resource constraints have often inhibited my progress yet I eagerly anticipate collaborative research that contributes substantively to the field. ''')

c1.write('''[LinkedIn](https://www.linkedin.com/in/ketan-suhaas-saichandran-050638245/) | [GitHub](https://github.com/Ketansuhaas)''')



c2.image("pic.jpeg",width= 400)

st.sidebar.success("Select a page above")


