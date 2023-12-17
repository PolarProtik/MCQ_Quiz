# frontend_interface.py

import streamlit as st
from backend_logic import generate_quiz

def main():
    st.title("MCQ Quiz Application")

    # Get user input for quiz topic and number of questions
    quiz_topic = st.text_input("Enter your preferred quiz topic:")
    num_questions = st.number_input("Enter the number of questions:", min_value=1, step=1)

    if st.button("Generate Quiz"):
        # Generate quiz data
        quiz_data = generate_quiz(quiz_topic, num_questions)

        # Display questions and options
        for i, question_data in enumerate(quiz_data, 1):
            st.write(f"**Question {i}:** {question_data['question']}")
            for j, option in enumerate(question_data['options'], 1):
                st.radio(f"Option {j}", option, key=f"{i}-{j}")

        # User submits quiz
        if st.button("Submit Quiz"):
            score = 0
            for i, question_data in enumerate(quiz_data, 1):
                selected_option = st.session_state[f"{i}-{j}"]
                if selected_option == question_data['correct_answer']:
                    score += 1

            # Display score
            st.write(f"Your Score: {score}/{num_questions}")
            st.write("Correct Answers:")
            for i, question_data in enumerate(quiz_data, 1):
                st.write(f"Question {i}: {question_data['options'][question_data['correct_answer']]}")

if __name__ == "__main__":
    main()
