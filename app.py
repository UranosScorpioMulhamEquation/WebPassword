import streamlit as st

# الحفاظ على دالة التوليد والمعادلات الرياضية بالكامل دون أي تعديل
def generate_password(machine_id_hex):
    digits = ''.join(filter(str.isdigit, machine_id_hex))
    if not digits: 
        try:
            digits = str(int(machine_id_hex, 16))
        except:
            return "Error"
    num = int(digits)
    result = round(abs(num / 2 * 3.14))
    return str(result)[:6]

# إعدادات الصفحة الخاصة بـ Streamlit لتشبه تنسيق flet الأصلي
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# تصميم واجهة المستخدم
st.title("Password Generator Tool")

# حقل إدخال معرف الجهاز
machine_id_input = st.text_input("Paste Machine ID", placeholder="Enter your hex code here...")

# زر التوليد ومنطق معالجة الحدث عند الضغط عليه
if st.button("Generate", type="primary"):
    if machine_id_input.strip() == "":
        st.warning("الرجاء إدخال Machine ID أولاً.")
    else:
        password = generate_password(machine_id_input)
        
        if password == "Error":
            st.error("خطأ: صيغة الـ Machine ID غير صحيحة.")
        else:
            # عرض النتيجة بتنسيق بارز ولون مخصص
            st.markdown(f"### Activation Password: <span style='color:blue;'>{password}</span>", unsafe_allow_html=True)