import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_batik_icon.png")
st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")

# SET TITLE AND LOGO IMAGE
intro_col_left, intro_col_right = st.columns(2)
intro_col_left.image('Bata Baca.png')
intro_col_right.markdown('<div style="text-align: justify; font-size:250%"> <b>Web App Klasifikasi Gambar Motif Batik</b> </div>',
            unsafe_allow_html=True)

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App ini merupakan suatu aplikasi web di mana kita bisa mengklasifikasikan suatu gambar motif batik ke dalam suatu jenis batik tertentu. Tidak hanya itu, aplikasi web ini juga memiliki fitur infopedia yang diharapkan dapat menambah wawasan pengguna mengenai budaya batik yang ada di Indonesia. </div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Bata Baca merupakan kependekan dari Batik Kita Batik Cita. Web App ini merepresentasikan batik kita (Indonesia) yang memiliki fitur untuk mendeteksi motif batik suatu daerah di Indonesia. Dengan adanya Web App ini, kami punya harapan atau cita agar batik dapat lebih dikenal dan dilestarikan oleh masyarakat. </div>',
            unsafe_allow_html=True)

# ANGGOTA TIM
st.write('## Anggota Tim :')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

foto_adam = Image.open('foto_adam.jpg').resize((400,400))
foto_alya = Image.open('Bebeb batik.jpg').resize((400,400))
foto_hanif = Image.open('foto_hanif.jpg').resize((400,400))
foto_naura = Image.open('foto_naura.png').resize((400,400))

# For columns 1 : Introduce Adam Maurizio Winata
col1.write('### Adam Maurizio Winata')
col1.image(foto_adam, caption = "Web App Developer")

# For columns 2 : Introduce Annaura Nabilla Masduki
col2.write('### Annaura Nabilla Masduki')
col2.image(foto_naura, caption = "Front-End Developer")

# For columns 3 : Introduce Muhammad Hanif Sudibyo
col3.write('### Muhammad Hanif Sudibyo')
col3.image(foto_hanif, caption = "Data Scientist")

# For columns 4 : Introduce Najma Attaqiya Alya
col4.write('### Najma Attaqiya Alya')
col4.image(foto_alya, caption = "Front-End Developer")