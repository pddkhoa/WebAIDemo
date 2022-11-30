import streamlit as st
from PIL import Image
import requests
from pathlib import Path
from streamlit_lottie import st_lottie

# ----- PATH SETTING -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "css" / "main.css"
pic_profile = current_dir / "assets" / "khoa.png"


# ----- GENERAL -----
PAGE_TITLE = "DIGITAL CV | DANG KHOA"
PAGE_ICON = ":wave:"
NAME = "PHAN DAI DANG KHOA"
DESCRIPTION = """
Tên tôi là Phan Đại Đăng Khoa, hiện là sinh viên đại học. Bằng sự nỗ lực, nhiệt tình và có trách nhiệm tôi mong muốn mình sẽ trở thành một Front End Developer.
"""
EMAIL = "khoadang88vn@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/pddkhoa",
    "Facebook": "https://www.facebook.com/khoadang.88.3154284/",
    "Instagram": "https://www.instagram.com/pdd.khoaa/",

}
st.set_page_config(page_icon=PAGE_ICON, page_title=PAGE_TITLE)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_mail = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_u25cckyh.json")

st.title("Hello Everyone!")

# ---Load CSS----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
pic_profile = Image.open(pic_profile)


# ----Hero Section---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(pic_profile, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(":mailbox:", EMAIL)


# --- Social Section----
st.write("---")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ----- GOAL ----
st.write("#")
st.subheader(":sparkles: MỤC TIÊU NGHỀ NGHIỆP")
st.write(
    """
    - :arrow_forward: Mong muốn trở thành một Front End Developer.
    - :arrow_forward: Mong muốn được cống hiến hết khả năng của bản thân. 
"""
)

# ---- SKILLL ----
st.write("#")
st.subheader(":star: KĨ NĂNG MỀM")
st.write(
    """
    - Có khả năng làm việc nhóm
    - Có khả năng kết nối mọi người
    - Luôn có trách nhiệm với công việc
    - Có kĩ năng giao tiếp và thuyết trình
"""
)

# ---- SKILLL ----
st.write("#")
st.subheader(":star: KĨ NĂNG CỨNG")
st.write(
    """
    - Programming: Java, C/C++, HTML, CSS, JavaScript
    - Database: MySQL, SQL
    - Other: Photoshop
"""
)

# ---- STUDY ----
st.write("#")
st.subheader(":school_satchel: HỌC VẤN")
st.write("Chuyên ngành: Công nghệ phần mềm")
st.write(" :arrow_forward: 2020 - Đến nay")


st.write("Đồ án")
st.write("""
    - :white_check_mark: Từ điển Anh-Việt
    - :white_check_mark: Phần mềm quản lí cửa hàng bán giày
    - :white_check_mark: Web thương mại điện tử chuyên về đấu giá nghịch
    - :white_check_mark: Web xem phim
""")
with st.container():
    st.write("---")
    st.header("Liên lạc với tôi!")
    st.write("##")
    contact_form = """
        <form action="https://formsubmit.co/khoadang88@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_mail, height=300, key="mail")
