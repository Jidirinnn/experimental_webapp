#changing the appearance of the webapp
#The arrangement of the code is the arrangement of appearance of the webapp. ==> it follows how the codes are chronologically ordered.

import streamlit as st                                                          #module to create web app
import functions as ft

todos = ft.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    ft.write_todos(todos)

st.title("My Todo App")
st.subheader("Jed's Todo-List Web Application")
st.write("<b>This app helps you to monitor your tasks.</b>",                                                            #<b> in HTML means bold letters
         unsafe_allow_html=True)                                                                                         #this line must be added below. It cannot be on the same line. Means allowing html codes to apply in the program

st.text_input(label='', placeholder='Add a new task...', on_change=add_todo, key='new_todo')

for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        ft.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.write('<marquee>"Curse of the self-taught: fear that you know only points here and there, islands of knowledge, and between them are chasms into which you will fall in humiliating failure, a fear that followed me from the first time I learned how to code." – Ellen Ullman, Life in Code</marquee>',
         unsafe_allow_html=True)
