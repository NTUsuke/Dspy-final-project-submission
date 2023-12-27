import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")




# Select a page in the sidebar
page = st.sidebar.selectbox("Choose a Page", ["Home", "COREFL ++"])

# Display content based on the selection
if page == "Home":
    import streamlit as st

    st.title('Final Project Demo App')
    st.subheader("Exploring English Learners Data: Python-Based Statistical Analysis and Data Visualization of the COREFL (Corpus of English as a Foreign Language)")
    st.write('程式設計與資料科學導論(Dspy)')


    members_markdown = """
    | 學號 | Name | 名字 | 系所 | 年級 | 負責 |
    |  ----  | ----  | ----  | ----  | ----  |----  |
    | R11142011 | Yusuke Taira | 平雄介 | 語言所 | 碩二 | statistical analysis
    | R10142010 | Mikhail Stepanenko | 米哈伊爾 | 語言所 | 碩三 | statistical analysis
    | R11142010 | Micah Kitsunai | 橘内每歌 | 語言所 | 碩二 | create application

    """
    st.markdown(members_markdown)


    st.write('')
    st.link_button("COREFL", 'http://corefl.learnercorpora.com/')

    st.markdown("> COREFL, standing for Corpus of English as a Foreign Language, is a comprehensive database that encompasses language produced by individuals learning English as a second or foreign language. A distinctive aspect of COREFL is that it includes both written and spoken data. A notable feature of the spoken data is its pairing with corresponding written texts. Each spoken text is linked to a written text by the same participant, who completed the same task in both formats. Initially, the participant creates the written text, followed by the spoken text after a minimum gap of 15 days to minimize repetition effects. This unique setup allows researchers to explore the impact of medium (spoken vs. written language) while keeping the learner and task consistent. _-[What is COREFL?](http://corefl.learnercorpora.com/)_")

    st.write('Chaplin youtube: ','https://youtu.be/eO1HvF2G2Sw?si=YYsvgScwzDREkz-P')
    video_url = 'https://youtu.be/eO1HvF2G2Sw?si=YYsvgScwzDREkz-P'

    st.video(video_url)

# elif page == "COREFL ++":

