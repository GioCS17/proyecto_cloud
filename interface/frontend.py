import streamlit as st
import requests
from io import StringIO
import json

st.set_page_config(layout="wide")

header = st.container()
code_string = ""

model_url = "http://172.17.0.3:9999/predict"

with header:
    st.title("Take care of you code - Detect vulnerabilities and save your life")

col1, col2 = st.columns(2) 

results = None

with col1:
    st.header("Insert your code")
    st.text("It is allowed just C and C++ code.")
    code_area = st.empty()
    code_string = code_area.text_area("", "", height = 400)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(bytes_data.decode("utf-8"))
        txt = stringio.read()
        code_string = code_area.text_area("", txt)
    st.write(code_string)

    if st.button('Send'):
        jsondata = json.dumps({'instance': code_string})
        response = requests.post(model_url, json=jsondata)
        results = json.loads(response.text)
        results = results["prediction"]
        print(type(results))
        #results = model.classify(code_string)
        print(results)

with col2:
    st.header("Predictions")

    st.subheader("CWE-119")
    if results is not None:
        val_pred = int(100*results['CWE-119'])
        if val_pred <= 30:
            st.success('Low!')
        elif val_pred <= 70:
            st.warning('Medium!')
        else:
            st.error('High')

        with st.expander("More explanation"):
            cwe119 = st.slider('Prediction Value', 0, 100, val_pred, help="Info sobre CWE-119..")
            st.write("""
                CWE-119 : The software performs operations on a memory buffer, but it can read from or write to a memory location that is outside of the intended boundary of the buffer.
                """)
            link='Check out this [link about CWE-119](https://cwe.mitre.org/data/definitions/119.html)'
            st.markdown(link,unsafe_allow_html=True)

    st.subheader("CWE-120")
    if results is not None:
        val_pred = int(100*results['CWE-120'])
        if val_pred <= 30:
            st.success('Low!')
        elif val_pred <= 70:
            st.warning('Medium!')
        else:
            st.error('High')
        with st.expander("More explanation"):
            cwe120 = st.slider('Prediction Value', 0, 100, val_pred, help="Info sobre CWE-120..")
            st.write("""
                CWE-120 : The program copies an input buffer to an output buffer without verifying that the size of the input buffer is less than the size of the output buffer, 
                leading to a buffer overflow.
                """)
            link='Check out this [link about CWE-120](https://cwe.mitre.org/data/definitions/120.html)'
            st.markdown(link,unsafe_allow_html=True)

    st.subheader("CWE-469")
    if results is not None:
        val_pred = int(100*results['CWE-469'])
        if val_pred <= 30:
            st.success('Low!')
        elif val_pred <= 70:
            st.warning('Medium!')
        else:
            st.error('High')
        with st.expander("More explanation"):
            cwe469 = st.slider('CWE-469', 0, 100, val_pred, help="Info sobre CWE-469..")
            st.write("""
                CWE-469 : The application subtracts one pointer from another in order to determine size, but this calculation can be incorrect if the pointers do not exist in the same memory chunk.
                """)
            link='Check out this [link about CWE-469](https://cwe.mitre.org/data/definitions/469.html)'
            st.markdown(link,unsafe_allow_html=True)

    st.subheader("CWE-476")
    if results is not None:
        val_pred = int(100*results['CWE-476'])
        if val_pred <= 30:
            st.success('Low!')
        elif val_pred <= 70:
            st.warning('Medium!')
        else:
            st.error('High')
        with st.expander("More explanation"):
            cwe476 = st.slider('CWE-476', 0, 100, val_pred, help="Info sobre CWE-476..")
            st.write("""
                CWE-476 : A NULL pointer dereference occurs when the application dereferences a pointer that it expects to be valid, but is NULL, typically causing a crash or exit.
                """)
            link='Check out this [link about CWE-476](https://cwe.mitre.org/data/definitions/476.html)'
            st.markdown(link,unsafe_allow_html=True)

    st.subheader("CWE-Other")
    if results is not None:
        val_pred = int(100*results['CWE-other'])
        if val_pred <= 30:
            st.success('Low!')
        elif val_pred <= 70:
            st.warning('Medium!')
        else:
            st.error('High')
        with st.expander("More explanation"):
            cweother = st.slider('CWE-Other', 0, 100, val_pred, help="Info sobre CWE-Other..")
            st.write("""
                CWE-Other : Improper Input Validation, Use of Uninitialized Variable, Buffer Access with Incorrect Length Value, etc. CWE 20, 457, 805 etc.
                """)
            link='Check out this [link about CWE-20](https://cwe.mitre.org/data/definitions/20.html)'
            st.markdown(link,unsafe_allow_html=True)
            link2='Check out this [link about CWE-457](https://cwe.mitre.org/data/definitions/457.html)'
            st.markdown(link2,unsafe_allow_html=True)
            link3='Check out this [link about CWE-805](https://cwe.mitre.org/data/definitions/805.html)'
            st.markdown(link3,unsafe_allow_html=True)


