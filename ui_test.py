import streamlit as st

# Заглавие и описание
st.title("🌿 Yard Greening Calculator")
st.write("Изчисли крайната цена и отстъпката за озеленяване на двор:")

# Полета за въвеждане
yards = st.number_input("✅ Квадратни метри за озеленяване:", min_value=0.0, format="%.2f")
price_per_yard = st.number_input("💰 Цена на кв. метър (лв):", min_value=0.0, value=7.61, format="%.2f")
discount = st.number_input("🎁 Отстъпка (%):", min_value=0.0, max_value=100.0, value=18.0, format="%.2f")

# Бутон за изчисление
if st.button("Изчисли"):
    # Пресмятания
    total_sum = yards * price_per_yard
    final_discount = total_sum * (discount / 100)
    final_sum = total_sum - final_discount

    # Резултат
    st.success(f"Крайна цена: {final_sum:.2f} лв.")
    st.info(f"Отстъпка: {final_discount:.2f} лв.")
