import streamlit as st
import pandas as pd
st.title("Welcome")
st.header("I m Neel Patel")
st.subheader("this is python website")
st.markdown("I love Python")
st.code("""
        for i in range(1,5,1)
        print(i)
        """)

dataset=pd.read_csv("q2fy24-investor-sheet.csv")
st.dataframe(dataset)
name=st.text_input("Enter Name:")
address=st.text_area("Area:")
classdata=st.selectbox("Enter class",(1,2,3,4,5,6,7,8,9))
button=st.button("OK")
if button:
    st.markdown(f"""
    Name:{name}Address:{address}
    class:{classdata}
                """)