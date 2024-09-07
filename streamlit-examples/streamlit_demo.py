import time

import streamlit as st

if "photo" not in st.session_state:
    st.session_state["photo"] = "Not done"

col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown("# Welcome to my app!")
col1.markdown("Here is some info on my app")


def change_photo_state():
    st.session_state["photo"] = "Done"


uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "Done":
    progress_bar = col2.progress(0)
    for percentage_completed in range(100):
        time.sleep(0.02)
        progress_bar.progress(percentage_completed + 1)

    col2.success("Photo uploaded successfully!")

    col3.metric(label="Temperature", value="72°F", delta="2°F")

    with st.expander("See more"):
        st.write("This is more information about the app")

        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)
