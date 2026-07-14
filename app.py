import streamlit as st

# ==================== إعدادات الصفحة الأساسية ====================
# يجب أن يكون هذا الأمر هو الأول دائماً في Streamlit
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# ==================== نظام التحقق من الهوية ====================
# تهيئة متغير الجلسة للتحقق مما إذا كان المستخدم قد سجل دخوله سابقاً
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# دالة التحقق من كلمة المرور
def check_password():
    st.title("🔒 نظام الوصول الآمن")
    st.write("الرجاء إدخال كلمة المرور لفتح أداة توليد كلمات المرور:")
    
    # حقل إدخال كلمة المرور (مخفية كرموز)
    password_input = st.text_input("كلمة المرور", type="password", placeholder="أدخل كلمة المرور هنا...")
    
    if st.button("دخول", type="primary"):
        if password_input == "1981":
            st.session_state["authenticated"] = True
            st.success("تم التحقق بنجاح! جاري تحويلك...")
            st.rerun()  # إعادة تشغيل الصفحة فوراً لإظهار الأداة
        else:
            st.error("كلمة المرور غير صحيحة! يرجى المحاولة مرة أخرى.")

# ==================== منطق الأداة الأساسي ====================

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

# التحقق من حالة الدخول وعرض الواجهة المناسبة
if not st.session_state["authenticated"]:
    # إذا لم يسجل الدخول، اعرض واجهة قفل التطبيق
    check_password()
else:
    # إذا تم التحقق بنجاح، اعرض التطبيق الأساسي بالكامل
    st.title("Password Generator Tool")
    
    # زر إضافي لتسجيل الخروج وإعادة قفل التطبيق عند الحاجة
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("قفل 🔓", help="تسجيل الخروج وقفل الأداة"):
            st.session_state["authenticated"] = False
            st.rerun()

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
