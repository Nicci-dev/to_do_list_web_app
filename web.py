import streamlit as st
import functions


to_do_list = functions.get_to_do_list()


def add_task():
    new_task = st.session_state["new_task"]  + "\n"
    to_do_list.append(new_task) 
    functions.write_to_do_list(to_do_list)



st.title("To-do list App")
st.subheader("Getting shit done.")
st.text("If it's not on the list it doesn't happen, so put it on the fucking list!")

for index, task in enumerate(to_do_list):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        to_do_list.pop(index)
        functions.write_to_do_list(to_do_list)
        del st.session_state[task]
        st.rerun()


st.text_input(label=" ", placeholder="Enter a task",
              on_change=add_task, key="new_task")
