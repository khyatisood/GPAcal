import streamlit as st
st.title("GPAcalculator")
st.header("FOR ELECTRONICS AND COMMUNICATION STUDENTS")
option = st.selectbox('ENTER YOUR COLLEGE/ORGANISATION/INSTITUTE NAME', ('Bhagwan Parshuram Institute of Technology', 'Maharaja Agrasen Institute of Technology', 'Bharatiya Vidyapeeth', 'Maharaja Surajmal Institute of Technology', 'USICT'))
st.write('You selected:', option)


def grades(marks):
    if marks >= 90:
        gradept = 10
    elif marks >= 75:
        gradept = 9
    elif marks >= 65:
        gradept = 8
    elif marks >= 55:
        gradept = 7
    elif marks >= 50:
        gradept = 6
    elif marks >= 45:
        gradept = 5
    elif marks >= 40:
        gradept = 4
    else:
        gradept = 0
    return gradept

def calc(semester):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0
    credits = 0
    col1, col2 = st.columns(2)
    if semester == 1:
        subjects = {"Applied Mathematics-I": 4, "Applied Physics-I": 3, "Manufacturing Processes": 3, "Electrical Technology": 3, "Human Values and Ethics-I": 1, "Fundamentals of Computing": 2 ,"Applied Chemistry": 3}
        labs = {'Applied Physics Lab-I': 1, 'Elecrical Tech. Lab': 1, 'Workshop': 2, 'Engineering Drawing': 2, 'Fundamentals of Computing Lab': 1, 'Applied Chemistry Lab': 1}
        credits = 27
    if semester == 2:
        subjects = {"Applied Mathematics-II": 4, "Applied Physics-II": 3, "Electronic Devices": 3, "Introduction to Programming": 3, "Engineering Mechanics": 3, "Communication Skills": 3, "Environmental Studies": 3}
        labs = {'Applied Physics Lab-II': 1, 'Programming Lab': 1, 'Electronic Devices Lab': 1, 'Engineering Mechanics Lab': 1, 'EVS Lab': 1}
        credits = 27
    if semester == 3:
        subjects = {"Applied Mathematics-III": 4, "Analog Electronics-I": 4, "Switching Theory and Logic Design": 4, "Electronic Instruments and Measurements": 4, "Data Structures": 4, "Signals and Systems": 4}
        labs = {'Analog Electronics lab': 1, 'STLD lab': 1, 'Electronic Instruments and Measurements Lab': 1, 'Data structures Lab': 1, 'signals and Systems Lab': 1}
        credits = 29
    if semester == 4:
        subjects = {"Applied Mathematics-IV": 4, "Analog Electronics-II": 4, "Network Analysis and Synthesis": 4,"Communication Systems": 4, "Electromagnetic Field Theory": 3, "Computer Organization and Architecture": 3}
        labs = {'Applied Mathematics-IV Lab': 1, 'Analog Electronics-II Lab': 1, 'Network Analysis and Synthesis Lab': 1, 'Communication Systems Lab': 1, 'Computer Organization and Architecture Lab': 1}
        credits = 28
    if semester == 5:
        subjects = {'Communication Skills for Professionals': 1, 'Digital Communication': 4, 'Microprocessors and Microcontrollers': 4, 'Control Systems': 4, 'Digital System Design': 4, 'Industrial Management': 3}
        labs = {'Communication Skills for Professionals Lab': 1, 'Digital Communication Lab': 1, 'Microprocessors and Microcontrollers Lab': 1, 'Control Systems Lab': 1, 'Digital System Design Lab': 1, 'Industrial/In-house training': 1}
        credits = 26
    if semester == 6:
        subjects = {"Microwave Engineering":4, "Information Theory and Coding": 4, "Digital Signal Processing": 4, "VLSI Design": 4, "Data Communication and Networks": 4, "Antenna and Wave Propagation": 4}
        labs = {"Microwave Engineering Lab": 1, "Digital Signal Processing Lab": 1, "VLSI Design Lab": 1, "Data Communication Networks Lab": 1, "Industrial/In-house training": 1}
        credits = 29
    if semester == 7:
        subjects = {"Embedded Systems": 4, "Optoelectronics and Optical Communication": 4, "Wireless Communication": 4, "Chosen subject from Group-A":3, "Chosen subject from Group-B":3}
        labs={"Optoelectronics and Optical Communication Lab":1 , "Embedded Systems Lab":1 , "lab based on elective I and/or II":1, "seminar":1, "Minor Project":3 , "Industrial training":1}
        credits=26
    if semester == 8:
        subjects={"Human Values and Professional Ethics-II":1 ,  "Satellite Communication":4 ,"Ad Hoc and Sensor Networks":3  , "Chosen subject from Group-A":3 , "Chosen subject from Group-B":3}
        labs={"Satellite and Antenna Lab":1, "Practical based on elective or Compulsory subject":1 , "Major project":8}
        credits=24

    with col1:
        with st.expander("Theory Subjects"):
            for subject in subjects:
                marks = st.slider("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * subjects[subject]

    with col2:
        with st.expander("Practical Subjects"):
            for lab in labs:
                marks = st.slider("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * labs[lab]
    if flag:
        st.warning("You cannot leave any field empty!")

    GPA = GPA / credits
    return GPA

name=st.text_input("Enter your name")
if name!="":
    st.write("Hello {}!".format(name))
semester = st.radio("Enter your semester number ", (1,2,3,4,5,6,7,8,))


st.markdown("<h3 style='text-align: center; '>ENTER MARKS</h3>", unsafe_allow_html=True)

GPA = calc(semester)

st.write("")
st.write("")

cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9)
with cl5:
    ans = st.button("Submit")

if ans:
    msg = "Your GPA: {}".format(str(round(GPA, 2)))
    st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
    if GPA >= 7.0:
        st.snow()
        st.balloons()

