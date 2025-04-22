import streamlit as st
import datetime
import calendar

st.title("My Demo Application")
st.subheader("This is my first time working with streamlit.Lets roll!")
name = st.text_input(label="Name")
if name:
    st.write(f"Welcome to streamlit {name}")

dob = st.date_input(label="Date of Birth",format="DD-MM-YYYY",min_value=datetime.date(1900,1,1),value=None)
if dob:
    day_of_week = calendar.day_name[dob.weekday()]
    month = dob.strftime("%B")
    day = dob.day
    
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1] if day % 10 <= 3 else "th"
    
    year = dob.year

    formatted_date = f"{day_of_week} {month} {day}{suffix}, {year}"
    st.write(f"Your were born on {formatted_date}")

gender = st.selectbox("Gender",["Male","Female","Rather Not Say"],placeholder="select-an-option",index=None)

if gender == "Male":
    st.write("You are a MAN")
elif gender == "Female":
    st.write("You are a WOMAN")
elif gender == "Rather Not Say":
    st.write("You are RETARDED")