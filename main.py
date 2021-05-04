import streamlit as st
import time

st.title('Streamlit入門')
# st.write('DataFrame')
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.dataframe(df.style.highlight_max(axis=0))
# st.map(df)


st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

left_column, right_column = st.beta_columns(2)

button = left_column.button('ボタン')
if button:
    right_column.write('右カラムです')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容をかく')
expander.button('ボタン１')
# if st.checkbox('Show Image'):
#     img = Image.open('river.jpg')
#     st.image(img, caption='Caption', use_column_width=True)

# select_option = st.selectbox(
#     'あなたが好きな数字は？',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', select_option, 'です'

# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は', text, 'です'

# slider = st.slider('あなたの調子は？', 0, 100, 0)
# st.write('あなたの調子は', slider, 'です')


for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
