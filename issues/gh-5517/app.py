import streamlit as st

count_of_files = 60
progress_bar = st.progress(0.0)
counter = 0
file_paths = [str(i) for i in range(count_of_files)]

try:
    for file in file_paths:
        progress_value = counter + (1 / count_of_files)
        if progress_value > 1.0:
            progress_value = 1.0
        progress_bar.progress(progress_value)
        counter += float(1 / count_of_files)
except st.StreamlitAPIException as e:
    st.error(f"Error: {e}")
