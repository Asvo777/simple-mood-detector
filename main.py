import streamlit as st
from textblob import TextBlob as tb

st.title(":red[Mood] Detector")
st.divider()

name = st.text_input("In one word, describe how you feel today")
testimonials = tb(name)

if name:
    st.write("Your sentiment polarity is: ", testimonials.sentiment.polarity)
    if(testimonials.sentiment.polarity < -0.6):
        st.write("I'm sorry to hear that you're feeling down. Remember, it's okay to have tough days. Take care of yourself!")
    elif(testimonials.sentiment.polarity < -0.2):
        st.write("I understand that you're going through a bit of a rough patch. Hang in there, and remember that things will get better.")
    elif(testimonials.sentiment.polarity < 0.2):
        st.write("Looks like you feel neutral today. Take some time for yourself and do something that makes you happy.")
    elif(testimonials.sentiment.polarity < 0.5):
        st.write("It's good to hear that you're feeling okay. Keep focusing on the positive aspects of your life and take care of yourself.")
    else:
        st.write("That's great to hear! Keep up the positive vibes and continue to take care of yourself.")
    if testimonials.sentiment.polarity > 0.2:
        st.balloons()