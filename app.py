from pathlib import Path 
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Marcin_Potoczny.pdf"
profile_pic = current_dir / "assets" / "marcin_potoczny.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Potoczny Marcin"
PAGE_ICON = ":wave:"
NAME = "Potoczny Marcin"
DESCRIPTION = """ 
Python Developer 
"""
EMAIL = "marcin.potoczny@protonmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/marpot",
    "LinkedIn": "https://www.linkedin.com/in/marcinpotoczny",
}
PROJECTS = {
    ":trophy: Puddle ecommerce app - online fullstack trading platform in python and django. User can sell items,add items,buy items,create account,login. Administration panel can manage users,delete users,add items,images,change prices. For frontend I used Tailwind CSS framework.": "https://github.com/marpot/Online-Marketplace"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    
    st.write(":email:", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    

# Experience and Qualifications
st.subheader("Experience")
st.write(":sparkles:", "Sales specialist | Selvoy" )
st.write("""
          March 2023 - September 2023 - Telephone sales of dietary supplements.Remote work.
         """)


st.write(":sparkles:", "NLP Solution Designer | Alfavox Sp. z o. o. Poznań" )
st.write("October 2022 - March 2023")
st.write(
"""
		Creating and training chatbots and voicebots in the model.
		NLP training and testing "Alfa" software for call centers.
		SQL database management.
		The flagship project was a chatbot and voicebot for Ministry of Finance.
		Remote work.
""")

st.write(":sparkles:", "Order Picker | Pantos Logistics Tilburg" )
st.write("November 2021 - March 2022")
st.write(
"""		Work trip 5 monthly. 
  		Work in a warehouse in the Netherlands. Collecting orders using the "EPT" trolley and a hand scanner. 
  		6/11/2021 to 25/03/2022
""")

st.write(":sparkles:", "Salesman in the power tools department.| Mrówka PSB Andrychów" )
st.write("June 2021 - October 2021")
st.write(
"""
Mrówka PSB Andrychów - salesman in the power tools department. Customer service, 
sale of power tools and other goods from the construction industry (throughout the store).
 06/2021 to 10/2021.	
""")

st.write(":sparkles:", "Quality Controller | Arvato Bertelsmann Heijen" )
st.write("September 2020 - April 2021")
st.write(
"""
Quality Controller at the Sony warehouse in the Netherdlands. My duties were to check the accuracy of the items collected by the commissioners and the quality of the cabling used
in the production of PlayStation 5 and PlayStation 4.
""")

st.write(":sparkles:", "IT Specialist | ASD Systems sp.z.o.o." )
st.write("May 2020 - June 2020")
st.write(
"""
IT specialist. Internship. I was responsible 
for writing automatic tests of a web application for remote operation of vending machines in Python.
""")

st.write(":sparkles:", "Fitter at the production plant.| Andoria sp.z.o.o." )
st.write("June 2015 - April 2020")
st.write(
"""
Fitter at the production plant.Installation of diesel engines for elevators and escalators.
""")



    
# --- SKILLS ---

st.subheader("Skills")
skills_list =[
"-English B2",
"-Python",
"-Django",
"-Streamlit",
"-Flask",
"-SQL",
"-SQLAlchemy",
"-Automate testing",
"-Manual testing",
"-Writing testing scenarios",
"-Linux",
"-HTML5",
"-CSS3",
"-Tailwind CSS framework",
"-Bootstrap framework",
"-Jira",
"-Confluence",
"-Druid engine",	
"-Agile working methodology",
"-Redmine",
"-Creating Documentation",
"-ChatGPT",
]

for skill in skills_list:
    st.write(f"- {skill}")

st.write("#")
st.subheader("Projects")
st.write("---")
PROJECTS = {
     ":trophy: Social Network app": "[Link to GitHub](https://github.com/marpot/SocialNetwork) - Social Network Project. Still in progress. Fullstack application using Vue.js and Tailwind CSS for frontend and Django REST Framework for backend. ",
    ":trophy: Puddle ecommerce app": "[Link to GitHub](https://github.com/marpot/Online-Marketplace) - Online fullstack trading platform in Python and Django. Users can sell items, add items, buy items, create accounts, and log in. Administration panel manages users, deletes users, adds items, images, and changes prices. Frontend uses the Tailwind CSS framework.",
    ":trophy: Bug Tracker": "[Link to GitHub](https://github.com/marpot/BugTracker) - Application in Flask framework and Python for tracking bugs in software development.",
    ":trophy: SnakeAI": "[Link to GitHub](https://github.com/marpot/SnakeAI) - Machine learning snake game self-learning how to play to win. Used Pygame and PyTorch.",
    ":trophy: IDE": "[Link to GitHub](https://github.com/marpot/IDE) - Simple Python IDE built in Python and Tkinter framework.",
    ":trophy: Instagram Hashtag Generator": "[Link to GitHub](https://github.com/marpot/instagram_hashtag_generator) - Web application built in Streamlit with BeautifulSoup and Pandas to research and generate popular hashtags for Instagram.",
    ":trophy: Pong Game": "[Link to GitHub](https://github.com/marpot/BugTracker) - Ping-pong game using Pygame in Python with sounds.",
    ":trophy: Slot Machine": "[Link to GitHub](https://github.com/marpot/PongGame) - Gambling machine in pure Python simulating a real gambling machine.",
    ":trophy: QR Code Generator": "[Link to GitHub](https://github.com/marpot/QrcodeGenerator) - Script generating QR code with my GitHub profile link.",
    ":trophy: Login System": "[Link to GitHub](https://github.com/marpot/Login-System) - Simple login page in Flask framework. User authentication.",
    ":trophy: YouTube Downloader": "[Link to GitHub](https://github.com/marpot/YoutubeDownloader) - Simple script to download YouTube movies in Python.",
    ":trophy: Caffe-Menu": "[Link to GitHub](https://github.com/marpot/Caffe-Menu) - HTML5 and CSS3 Caffe menu.",
}

# Display projects using a card layout
for project, description in PROJECTS.items():
    st.write(f"## {project}")
    st.write(description)
    st.write("---")

