import streamlit as st

st.set_page_config(page_title="カラー剤コスト比較アプリ")

st.title("THAN vs 他カラー剤　コスト比較ツール")

col1, col2 = st.columns(2)

def get_inputs(title, col):
    st.subheader(title)
    g1 = col.number_input(f"{title}: 1剤容量(g)", value=120)
    p1 = col.number_input(f"{title}: 1剤価格(円)", value=360)
    g2 = col.number_input(f"{title}: 2剤容量(ml/g)", value=2000)
    p2 = col.number_input(f"{title}: 2剤価格(円)", value=1000)
    ratio = col.number_input(f"{title}: 混合比(1:x)", value=2)
    
    # 計算
    u1 = p1 / g1
    u2 = p2 / g2
    mixed_price = (u1 * 1 + u2 * ratio) / (1 + ratio)
    return mixed_price

with col1:
    price1 = get_inputs("THAN", col1)
with col2:
    price2 = get_inputs("比較対象", col2)

st.divider()
st.subheader("結果比較")
st.write(f"THAN 混合時単価: **{price1:.2f} 円/g**")
st.write(f"比較対象 混合時単価: **{price2:.2f} 円/g**")

if price1 < price2:
    st.success("THAN の方がお得です！")
elif price2 < price1:
    st.success("比較対象 の方がお得です！")
else:
    st.info("どちらも同じ単価です。")
