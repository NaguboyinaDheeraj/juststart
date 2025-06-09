import streamlit as st
import random

# Quiz questions for each language
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
    ],
    "Java": [
        {"question": "Which of these is the correct way to declare a variable in Java?", "options": ["int x;", "var x;", "x int;", "int: x;"], "answer": "int x;"},
        {"question": "What keyword is used to create a class in Java?", "options": ["class", "Class", "def", "function"], "answer": "class"},
        {"question": "Which method is the entry point of a Java program?", "options": ["start()", "main()", "run()", "execute()"], "answer": "main()"},
        {"question": "What does 'public static void main(String[] args)' mean?", "options": ["Method header", "Variable declaration", "Class definition", "Interface"], "answer": "Method header"},
        {"question": "Which operator is used for equality check in Java?", "options": ["=", "==", "===", "!="], "answer": "=="},
        {"question": "How do you print output in Java?", "options": ["System.out.println()", "print()", "console.log()", "echo"], "answer": "System.out.println()"},
        {"question": "Which of these is not a Java primitive data type?", "options": ["int", "float", "String", "boolean"], "answer": "String"},
        {"question": "What keyword is used to inherit a class in Java?", "options": ["extends", "implements", "inherits", "uses"], "answer": "extends"},
        {"question": "Which of these is used for comments in Java?", "options": ["//", "#", "<!-- -->", "/* */"], "answer": "//"},
        {"question": "What is the size of int in Java?", "options": ["16 bits", "32 bits", "64 bits", "Depends on system"], "answer": "32 bits"}
    ],
    "HTML/JavaScript": [
        {"question": "What does HTML stand for?", "options": ["Hyperlinks and Text Markup Language", "Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinking Text Management Language"], "answer": "Hyper Text Markup Language"},
        {"question": "Which tag is used to create a hyperlink in HTML?", "options": ["<link>", "<a>", "<href>", "<hyperlink>"], "answer": "<a>"},
        {"question": "How do you write a comment in HTML?", "options": ["// comment", "<!-- comment -->", "/* comment */", "# comment"], "answer": "<!-- comment -->"},
        {"question": "Which of these is a JavaScript data type?", "options": ["string", "boolean", "number", "All of the above"], "answer": "All of the above"},
        {"question": "How do you declare a variable in JavaScript?", "options": ["var x;", "int x;", "let x;", "Both var x; and let x;"], "answer": "Both var x; and let x;"},
        {"question": "Which symbol is used for single line comments in JavaScript?", "options": ["//", "#", "<!-- -->", "/* */"], "answer": "//"},
        {"question": "How do you create a function in JavaScript?", "options": ["function myFunc() {}", "def myFunc() {}", "func myFunc() {}", "create myFunc() {}"], "answer": "function myFunc() {}"},
        {"question": "What is the correct way to get an element by ID in JavaScript?", "options": ["document.getElementById()", "document.querySelector()", "document.getElement()", "getElementById()"], "answer": "document.getElementById()"},
        {"question": "Which attribute is used to include JavaScript code in HTML?", "options": ["<js>", "<script>", "<javascript>", "<code>"], "answer": "<script>"},
        {"question": "What is the correct HTML element for inserting a line break?", "options": ["<break>", "<br>", "<lb>", "<newline>"], "answer": "<br>"}
    ]
}

# Page config
st.set_page_config(
    page_title="GrowTech Quiz App",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Style
st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        font-weight:700;
        color: #4B8BBE;
    }
    .question {
        font-size:22px;
        font-weight:600;
        color: #306998;
    }
    .stButton>button {
        background-color: #FFD43B;
        color: black;
        font-weight: 600;
        border-radius: 10px;
        padding: 8px 18px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FFE873;
        color: black;
    }
    .correct {
        color: green;
        font-weight: 700;
        font-size: 18px;
    }
    .wrong {
        color: red;
        font-weight: 700;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and intro
st.markdown('<h1 class="big-font">🎓 GrowTech Quiz App</h1>', unsafe_allow_html=True)
st.markdown("Welcome! Select a programming language and test your knowledge with 10 questions. Good luck! 🍀")

language = st.selectbox("Select a programming language:", list(quizzes.keys()))

if "questions" not in st.session_state or st.session_state.get("language_selected") != language:
    st.session_state.questions = random.sample(quizzes[language], 10)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.language_selected = language
    st.session_state.quiz_finished = False

def next_question():
    if st.session_state.selected_option is None:
        st.warning("⚠️ Please select an option before submitting.")
        return
    q = st.session_state.questions[st.session_state.current_index]
    if st.session_state.selected_option == q['answer']:
        st.session_state.score += 1
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong! Correct answer: **{q['answer']}**")
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    if st.session_state.current_index >= len(st.session_state.questions):
        st.session_state.quiz_finished = True

if not st.session_state.quiz_finished:
    q = st.session_state.questions[st.session_state.current_index]
    st.markdown(f'<p class="question">Question {st.session_state.current_index + 1} of 10:</p>', unsafe_allow_html=True)
    st.markdown(f'### {q["question"]}')
    st.session_state.selected_option = st.radio("Select your answer:", q['options'], key="quiz_options")

    if st.button("Submit Answer"):
        next_question()
else:
    st.balloons()
    st.markdown(f"### 🎉 Quiz Finished!")
    st.markdown(f"Your final score is: **{st.session_state.score} / 10**")
    st.progress(st.session_state.score / 10)
    if st.button("Restart Quiz"):
        st.session_state.questions = random.sample(quizzes[language], 10)
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.quiz_finished = False

