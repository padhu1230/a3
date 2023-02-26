from email.mime import image
import os
import streamlit as st
import streamlit as st
from matplotlib import image as img
import plotly.express as px

file_directory=os.path.dirname(os.path.abspath(__file__))

parent_directory=os.path.join(file_directory,os.pardir)

dir_of_interest=os.path.join(parent_directory,"resources")




st.title(":orange[**_Everything in nature invites us constantly to be what we are_**]:heartpulse:")
imag1=img.imread(r"C:\Users\ASUS\Desktop\Internship\proj2\resourses\images\n1.jpg")
imag2=img.imread(r"C:\Users\ASUS\Desktop\Internship\proj2\resourses\images\n2.jpg")

st.markdown(":red[_**If you love nature, you will find beauty anywhere._**]")

st.image([imag1,imag2],width=300)
st.markdown(":red[**_“No other sound can match the healing power of the sounds of nature.”_**]")

#displaying a video by simply passing a Youtube link
st.video("https://youtu.be/rOor-3U45tI")

import streamlit as st

from PIL import Image
col1,col2=st.columns(2)
st.title(":red[My Profile]  :blue_heart:")

st.subheader(":pink[Padmavathi Devalla]   (data Science Intern At :red[Innomatic Reaserch Lab)]")
st.markdown("Badhrachalam ,telangana")
st.markdown("**Ph**:6302902227")
st.markdown("**Email**-devallapadhu@gmail.com")
st.markdown("**Linkedin**-  :https://www.linkedin.com/in/padmavathi-devalla-8940a4211")
st.markdown(":violet[**_Objective_** :]  To obtain a position as a Data Scientist in a collaborative environment utilizing my creativity and technical skills. The position must demand a high degree of self-motivation and the ability to drive data-centric solutions for complex business problems.")
