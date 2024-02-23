import streamlit as st


# Define the Streamlit app
def app():
    # Form 1 for user information
    form1 = st.form("user_info")
    name = form1.text_input("Enter your name")
    age = form1.number_input("Enter your age", min_value=0)
    submit1 = form1.form_submit_button("Submit")
    
    if submit1:
        st.write(f"Hello, {name}! You are {age} years old.")
    
    # Form 2 for feedback
    form2 = st.form("feedback")
    rating = form2.selectbox("Rate your experience", [1, 2, 3, 4, 5])
    feedback = form2.text_area("Tell us what you think")
    submit2 = form2.form_submit_button("Submit")
    
    if submit2:
        st.write("Thank you for your feedback!")

if __name__ == "__main__":
    app()
