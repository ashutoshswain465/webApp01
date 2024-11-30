import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    """
    Adds a new to-do item to the list if the input is valid (non-empty).
    """
    todo_web = st.session_state["new_todo"].strip()  # Remove whitespace
    if todo_web:  # Ensure input is not empty
        todos.append(todo_web + "\n")
        functions.write_todos(todos)


# This is a webapp
# Application UI
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Input field for adding a new to-do
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# Display current to-dos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)  # Strip newline characters for display
    if checkbox:
        todos.pop(index)  # Remove the completed todo
        functions.write_todos(todos)
        del st.session_state[todo]  # Remove the session state key
        st.rerun()  # Refresh the app to update the UI
