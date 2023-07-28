import plotly.express as px
df = px.data.iris()
df.head()

fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species", # Species 열의 값에 따라서 색깔 표현
                 size='petal_length', # petal_length 에 따라 크기를 변화
                 hover_data=['petal_width'], # 참고할 데이터 추가
                 title='Iris Data - Scatter Plot' # 그래프 타이틀 지정
                )
fig.show()