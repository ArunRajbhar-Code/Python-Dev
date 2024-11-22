import streamlit as st
st.header("To Do App")


with open("todo.txt","r") as file:
    todos=file.readlines()
for i in todos:
    st.checkbox(i,key=i)    
todo=st.text_input(label="Enter To Do" ,label_visibility="collapsed")    
with open("todo.txt","a") as file:
    file.write(todo+"\n")
