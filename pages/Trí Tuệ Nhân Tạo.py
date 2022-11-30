import pandas as pd
import time
import plotly.express as px
import streamlit as st
import streamlit as st
import requests
import plost
from PIL import Image
from streamlit_lottie import st_lottie
import base64
from io import StringIO, BytesIO


st.set_page_config(
    page_title="Trí Tuệ Nhân Tạo",
    layout="wide"

)


def local_css(file_name):
    with open("style.css") as soucre_des:
        st.markdown(f"<style>{soucre_des.read()}</style>",
                    unsafe_allow_html=True)


local_css("css/style.css")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----- LOAD ASSET ----
lottie_coding = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_o6spyjnc.json")
lottie_carrer = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_mail = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_u25cckyh.json")
img_contact = Image.open("./image/robot.jpg")

# ----- HEAD ------


def intro():
    with st.container():
        st.header("Ngành Trí tuệ nhân tạo")
        st.subheader("Trí tuệ nhân tạo (Artificial Intelligence) là gì?")
        st.write("""
    Trí tuệ nhân tạo (AI) là ngành tạo ra máy móc và hệ thống thông minh thông qua việc sử dụng mô hình máy tính, kỹ thuật và công nghệ liên quan,
    giúp thực hiện các công việc yêu cầu trí thông minh của con người. Nhìn chung, đây là một ngành học rất rộng, bao gồm các yếu tố tâm lý học, khoa học máy tính và kỹ thuật.
    Một số ví dụ phổ biến về AI có thể kể đến ô tô tự lái, phần mềm dịch thuật tự động, trợ lý ảo trên điện thoại hay đối thủ ảo khi chơi trò chơi trên điện thoại.
     """)

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader("Liệu bạn có phù hợp với ngành Trí tuệ nhân tạo?")

                st.write("##")
                st.write(
                    """
                Nếu bạn muốn theo đuổi sự nghiệp trong ngành trí tuệ nhân tạo, những phẩm chất sau sẽ giúp bạn gặt hái thành công trong ngành. Cùng tìm hiểu xem liệu bạn có phù hợp với ngành AI không nhé.

                1. Không ngừng tò mò và yêu thích sự sáng tạo
                2.  Khả năng "hiểu sâu" dữ liệu
                3. Kiên trì và nỗ lực không ngừng
                4. Khả năng học hỏi nhanh
                """
                )
            with right_column:
                st_lottie(lottie_coding, height=300, key="coding")

        with st.container():
            st.write("---")
            st.write("##")
            img_column, text_column = st.columns((1, 2))
            with img_column:
                st.image(img_contact)
            with text_column:
                st.subheader("Ngành Trí tuệ nhân tạo học những gì?")
                st.write("##")
                st.write(
                    """
                Nền tảng kiến thức về công nghệ máy tính và toán học là xương sống của hầu hết các chương trình trí tuệ nhân tạo.
                Sinh viên có thể lựa chọn các chương trình cấp bằng ngành trí tuệ nhân tạo hoặc theo đuổi chuyên ngành AI từ các ngành học như
                khoa học máy tính, thiết kế đồ họa, công nghệ thông tin hoặc kỹ thuật.

                Gồm các môn học:

                    -  Nguyên tắc cơ bản của trí tuệ nhân tạo
                    -  Các kỹ thuật toán học của trí tuệ nhân tạo
                    -  Nguyên lý lập trình và tính toán
                    -  Lý thuyết tính toán
                    -  Hệ thống và kiến trúc
                    -  Thiết kế thuật toán
                    -  Kỹ thuật phần mềm
                    -  Mạng thần kinh nhân tạo
                    -  Robot học (Robotics)
                """
                )

        with st.container():
            st.write("---")
            left_column, right_column = st.columns((1, 2))
            with right_column:
                st.subheader(
                    "Sinh viên ngành Trí tuệ nhân tạo làm gì khi ra trường?")

                st.write("##")
                st.write(
                    """

                1. Nhà nghiên cứu về trí tuệ nhân tạo (Artificial Intelligence Researcher)
                2. Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP)
                3. Kiến trúc sư AI (AI Architect)
                4. Kỹ sư dữ liệu lớn (Big Data Engineer)
                5. Kỹ sư học máy (Machine Learning Engineer)
                """
                )
            with left_column:
                st_lottie(lottie_carrer, height=300, key="carrer")
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


def mapping_demo():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plost
    from PIL import Image

    with open('demo.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        # Data
    seattle_weather = pd.read_csv(
        'https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv(
        'https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

    st.title("THỐNG KÊ THỜI TIẾT")
    # Row A
    a1, a2, a3 = st.columns(3)
    a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
    a2.metric("Wind", "9 mph", "-8%")
    a3.metric("Humidity", "86%", "4%")

    # Row B
    b1, b2, b3, b4 = st.columns(4)
    b1.metric("Temperature", "70 °F", "1.2 °F")
    b2.metric("Wind", "9 mph", "-8%")
    b3.metric("Humidity", "86%", "4%")
    b4.metric("Humidity", "86%", "4%")

    # Row C
    with st.container():
        st.markdown('### Heatmap')
        plost.time_hist(
            data=seattle_weather,
            date='date',
            x_unit='week',
            y_unit='day',
            color='temp_max',
            aggregate='median',
            legend=None)


def plotting_demo():
    import streamlit as st
    from streamlit_lottie import st_lottie

    lottie_computer = load_lottieurl(
        "https://assets3.lottiefiles.com/packages/lf20_iv4dsx3q.json")
    st.title("UPDATE DỮ LIỆU TỪ FILE EXCEL")

    df = pd.read_excel(
        io="Data1.xlsx",
        engine="openpyxl",
    )
    product = st.sidebar.multiselect(
        "Vui lòng chọn ít nhất một sản phẩm:",
        options=df["TenSanPham"].unique(),
        default=df["TenSanPham"].unique(),

    )

    df_selection = df.query(
        "TenSanPham == @product"
    )

    line_product = (
        df_selection.groupby(by=["TenSanPham"]).sum()[
            ["SoLuong"]].sort_values(by="SoLuong")
    )
    col1, col2 = st.columns((2, 1))
    with col1:
        st.write(df)
    with col2:
        st_lottie(lottie_computer, height=300)
    reload = st.button("Reload")

    st.sidebar.header("Options")
    options_form = st.sidebar.form("options_form")
    product_name = options_form.text_input("Tên Sản Phẩm")
    cout = options_form.text_input("Số Lượng")
    add_data = options_form.form_submit_button("Thêm")
    if add_data:
        new_data = {"TenSanPham": product_name, "SoLuong": int(cout)}
        df = df.append(new_data, ignore_index=True)
        df.to_excel("Data1.xlsx", index=False)

        progress_bar = st.progress(0)
        for perc_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(perc_complete+1)
        st.write("Đã thêm thành công!")
        st.sidebar.write("Thành Công!")
    if reload:
        st.experimental_rerun()
    with st.container():
        st.markdown("# Thống Kê")
        chart_product = px.bar(
            line_product,
            x=line_product.index,
            y="SoLuong",
            title="<b>Bảng Số Liệu Sản Phẩm</b>",
            color_discrete_sequence=["#0083B8"] * len(line_product),
            template="plotly_white"
        )
        chart_product.update_layout(
            xaxis=dict(tickmode="linear"),
            plot_bgcolor="rgba(0, 0, 0, 0)",
            yaxis=(dict(showgrid=False))
        )
        st.plotly_chart(chart_product)


def data_frame_demo():
    import streamlit as st
    import plotly.express as px
    import pandas as pd

    upload_file = st.file_uploader("Chosse a XLSX file: ", type="xlsx")

    if upload_file:
        st.markdown("---")
        df = pd.read_excel(upload_file, engine="openpyxl")
        st.header(
            """
            THỐNG KÊ DÂN SỐ
            CÁC NĂM 2016, 2017, 2018, 2019, 2020
        """
        )
        st.dataframe(df)
        groupby_column = st.selectbox(
            "Chọn Năm: ",
            ("NĂM 2016", "NĂM 2017", "NĂM 2018", "NĂM 2019", "NĂM 2020")
        )
        st.sidebar.header("Vui lòng lọc dữ liệu cần tìm")

        city = st.sidebar.multiselect(
            "Vui lòng chọn ít nhất một tỉnh thành:",
            options=df["TÊN_TỈNH"].unique(),
            default=df["TÊN_TỈNH"].unique(),

        )

        df_selection = df.query(
            "TÊN_TỈNH == @city"
        )

        output_columns = ["TÊN_TỈNH"]
        df_group = df_selection.groupby(by=[groupby_column], as_index=False)[
            output_columns].sum()
        st.markdown("""
            BẢNG SỐ LIỆU DÂN SỐ
        """)
        st.dataframe(df_group)

        fig = px.bar(
            df_group,
            x=groupby_column,
            y="TÊN_TỈNH",
            color_continuous_scale=["red", "yellow", "green"],
            template="plotly_white",
            title=f"<b>BIỂU ĐỒ SỐ LIỆU DÂN SỐ {groupby_column}</b>"
        )
        st.plotly_chart(fig)


page_names_to_funcs = {
    "Giới thiệu về AI": intro,
    "Update Dữ Liệu Excel": plotting_demo,
    "Thông Kê Thời Tiết": mapping_demo,
    "Thống Kê Dân Sô": data_frame_demo
}

demo_name = st.sidebar.selectbox("Chọn", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
