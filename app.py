import streamlit as st
import random

def simulate_gacha_fixed_targets(total_types, target_types, num_draws, num_trials):
    hits = 0
    for _ in range(num_trials):
        draws = [random.randint(1, total_types) for _ in range(num_draws)]
        if all(t in draws for t in target_types):
            hits += 1
    return hits / num_trials

st.title("🎯 缶バッジ狙い撃ちシミュレーション")
st.write("購入数と狙っている種類数を設定して、当たる確率を計算してみよう！")

total_types = st.number_input("缶バッジの総種類数", min_value=1, value=10)
num_targets = st.number_input("狙っている種類数", min_value=1, max_value=total_types, value=2)
num_draws = st.number_input("購入数", min_value=1, value=15)
num_trials = st.number_input("シミュレーション回数", min_value=100, value=100000, step=10000)

if st.button("シミュレーション実行"):
    target_types = random.sample(range(1, total_types + 1), num_targets)
    st.write(f"狙いの種類（固定）: {target_types}")
    prob = simulate_gacha_fixed_targets(total_types, target_types, num_draws, num_trials)
    st.success(f"{num_draws}個買ったとき、狙いの{num_targets}種が全て出る確率：{prob * 100:.2f}%")
