import streamlit as st
import requests,base64

st.set_page_config(page_title="EcoLens",layout="wide")
st.title("EcoLens AI")
st.write("Local Vision for Sustainable Disposal")

f=st.file_uploader("Upload waste image",type=['jpg','png','jpeg'])

if f:
    with st.spinner('Processing...'):
        res=requests.post("http://127.0.0.1:8100/analyze",files={"file":f.getvalue()})
        if res.status_code==200:
            d=res.json()
            col1,col2=st.columns(2)
            with col1:
                if d['img']:st.image(base64.b64decode(d['img']))
            with col2:
                st.subheader(f"Items: {d['labels']}")
                st.write(d['info'])
                
                # Simple logic for bin display
                txt=d['info'].lower()
                if "recycle" in txt:st.success("Target: 🟦 Recycling Bin")
                elif "hazard" in txt:st.warning("Target: 🚩 Special Disposal")
                else:st.error("Target: ⬛ General Waste")
        else:st.error("Connection error")