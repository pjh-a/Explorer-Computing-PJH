import streamlit as st
import pandas as pd

def showInfo():
    st.markdown("# 나의 자기소개 페이지")
    st.markdown("## 자기소개")
    st.markdown("안녕하세요, 제 이름은 " + "**박지효**" + "입니다.")
    st.markdown("## 좋아하는 것")
    st.write("*여행*을 좋아합니다.")
    st.markdown("[링크로 이동](https://naver.com)")
    st.markdown("## 코딩")
    st.code("print('hello')")
    st.latex("a^2=3")
    st.write(pd.DataFrame({"점수": range(90, 101, 2), "석차": range(1, 12, 2)}))

showInfo()
