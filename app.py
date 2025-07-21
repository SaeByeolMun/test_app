# 파일명: app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 간단한 데이터 시각화 앱")

st.write("슬라이더를 이용해 데이터 수를 선택하세요.")

# 슬라이더 위젯
n = st.slider("데이터 수", 10, 100, 50)

# 난수 데이터 생성
data = pd.DataFrame({
    'x': np.arange(n),
    'y': np.random.randn(n)
})

st.line_chart(data.set_index('x'))

# 파일 다운로드 버튼
csv = data.to_csv(index=False).encode('utf-8')
st.download_button("CSV로 저장", csv, "data.csv", "text/csv")
