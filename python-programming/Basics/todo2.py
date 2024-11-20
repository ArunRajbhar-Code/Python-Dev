import streamlit as st

st.header("To Do Application")
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_input("Enter the To Do",label_visibility="collapsed")
with col2:
    Adder=st.button("Add To Do")  
    if Adder:
            with open("todo.txt","a") as file:
                   file.write(user_input+"\n")
           
with col1:
    with open("todo.txt","r") as file:
                todos=file.readlines()
    for index,i in enumerate(todos):
                st.write(index+1,"-",i.removesuffix("\n"))
with col2:
       with open("todo.txt","r") as file:
              todos=file.readlines()
       for index, i in enumerate(todos):
              st.checkbox(f"complete{index}")                       

