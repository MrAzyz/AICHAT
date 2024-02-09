import streamlit as st
import LLM as llm

st.set_page_config(page_title="FREE CHAT",page_icon=":robot_face:",layout="centered")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


def main():
    st.title(":robot_face: Enter You Question here")
    
    # Get user question
    input_text = st.text_input("Enter some text: :book:")

    # Display answer text when button is clicked
    if st.button("answer"):
        #Warning if there is no input
        if not input_text:
            st.warning("Oops! It seems you forgot to enter a question. Please enter a question before clicking the 'Answer' button.")
        #display response
        else:
            st.write(llm.generate_response(input_text))
            st.download_button(
                label="Download Answer",
                data=llm.generate_response(input_text),
                file_name="answer.txt",
                mime="text/plain",
            )

if __name__ == "__main__":
    main()
