import streamlit as st
import random

quizzes = {
    "Python": [
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "12"], "answer": "8"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "function", "lambda"], "answer": "def"},
        {"question": "What data type is returned by the input() function?", "options": ["int", "string", "float", "bool"], "answer": "string"},
        {"question": "Which of these is a Python tuple?", "options": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "None of the above"], "answer": "(1, 2, 3)"},
        {"question": "What does 'list.append()' do?", "options": ["Removes item", "Adds item to end", "Sorts list", "Clears list"], "answer": "Adds item to end"},
        {"question": "What symbol is used for comments in Python?", "options": ["//", "#", "<!-- -->", "/* */"], "answer": "#"},
        {"question": "How do you create a dictionary in Python?", "options": ["[]", "()", "{}", "None"], "answer": "{}"},
        {"question": "Which keyword is used for loops in Python?", "options": ["loop", "for", "repeat", "iterate"], "answer": "for"},
        {"question": "How do you import a module named 'math'?", "options": ["import math", "include math", "using math", "require math"], "answer": "import math"},
        {"question": "What is the correct way to check equality in Python?", "options": ["=", "==", "===", "!="], "answer": "=="}
    ]
}

st.set_page_config(page_title="GrowTech Quiz", layout="centered")
st.title("🎓 GrowTech Quiz App")

language = st.selectbox("Choose language:", list(quizzes.keys()))

# Initialize session state when language changes or first run
if 'language' not in st.session_state or st.session_state.language != language:
    st.session_state.language = language
    st.session_state.questions = random.sample(quizzes[language], min(10, len(quizzes[language])))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answer_submitted = False
    st.session_state.selected_option = None
    st.session_state.quiz_finished = False
    st.session_state.history = []

def display_history():
    st.subheader("Your Answers So Far:")
    for i, entry in enumerate(st.session_state.history, start=1):
        st.markdown(f"**Q{i}:** {entry['question']}")
        st.markdown(f"**Your Answer:** {entry['answer']}")
        if entry['correct']:
            st.success("Correct")
        else:
            st.error(f"Wrong (Correct: {entry['correct_answer']})")
        st.markdown("---")

if not st.session_state.quiz_finished:
    q = st.session_state.questions[st.session_state.current]
    st.markdown(f"### Question {st.session_state.current + 1}: {q['question']}")

    if not st.session_state.answer_submitted:
        st.session_state.selected_option = st.radio("Choose an answer:", q["options"], key=f"answer_radio_{st.session_state.current}")
        if st.button("Submit Answer", key="submit_answer"):
            # Check answer
            if st.session_state.selected_option == q["answer"]:
                st.session_state.score += 1
                correct = True
            else:
                correct = False

            # Save answer details
            st.session_state.history.append({
                "question": q["question"],
                "answer": st.session_state.selected_option,
                "correct_answer": q["answer"],
                "correct": correct
            })
            st.session_state.answer_submitted = True
    else:
        # Show result for submitted answer
        last = st.session_state.history[-1]
        if last['correct']:
            st.success("Correct! ✅")
        else:
            st.error(f"Wrong! ❌ The correct answer is: {last['correct_answer']}")

        # Standalone Next Question button
        if st.button("Next Question", key="next_question"):
            st.session_state.current += 1
            st.session_state.answer_submitted = False
            st.session_state.selected_option = None

            if st.session_state.current >= len(st.session_state.questions):
                st.session_state.quiz_finished = True

    display_history()

else:
    st.balloons()
    st.header(f"Quiz Finished! Your score: {st.session_state.score} / {len(st.session_state.questions)}")
    display_history()

    if st.button("Restart Quiz", key="restart_quiz"):
        st.session_state.questions = random.sample(quizzes[language], min(10, len(quizzes[language])))
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False
        st.session_state.selected_option = None
        st.session_state.quiz_finished = False
        st.session_state.history = []