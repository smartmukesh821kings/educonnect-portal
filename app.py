import streamlit as st
import pandas as pd
import random
import time

# ==========================================
# 1. PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="EduConnect - Primary School Portal",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for primary school styling cards
st.markdown("""
<style>
    .mission-box {
        background-color: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 20px;
        border-radius: 4px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. FULLY SCALED FACULTY DATABASE (15 Teachers)
# ==========================================
TEACHERS_DATA = [
    # --- Class 1 Faculty ---
    {"id": "T1", "name": "Miss Emily Watson", "subject": "Class 1 Homeroom & Math", "bg": "B.Ed. in Early Childhood Education. 6 years teaching primary grades.", "tone": "gentle, encouraging, and uses emojis like 🌱 and ✨"},
    {"id": "T2", "name": "Mr. Arsam Khan", "subject": "Class 1 Science & Nature", "bg": "B.S. in Elementary Education. Focuses on interactive lab-based learning.", "tone": "enthusiastic about nature, highly curious, and uses emojis like 🔬 and 🦕"},
    {"id": "T3", "name": "Mrs. Clara Oswald", "subject": "Class 1 English & Arts", "bg": "B.A. in English Literature from Cambridge. Creative writing specialist.", "tone": "warm, artistic, expressive, and uses emojis like 🎨 and 📚"},
    
    # --- Class 2 Faculty ---
    {"id": "T4", "name": "Mrs. Sarah Jenkins", "subject": "Class 2 Homeroom & Science", "bg": "M.S. in Education. Specialist in interactive primary learning architectures.", "tone": "structured, supportive, and uses emojis like 🚀 and 🧪"},
    {"id": "T5", "name": "Mr. James Fletcher", "subject": "Class 2 Mathematics", "bg": "B.S. in Mathematics. Passionate about gamified foundational math.", "tone": "energetic, logic-driven, playful, and uses emojis like 🎲 and 📐"},
    {"id": "T6", "name": "Miss Lily Evans", "subject": "Class 2 Language Arts", "bg": "B.Ed. in Primary Education. Expert in early reading development.", "tone": "kind, patient, focused on vocabulary, and uses emojis like 📖 and ✏️"},
    
    # --- Class 3 Faculty ---
    {"id": "T7", "name": "Mr. David Kim", "subject": "Class 3 Homeroom & English", "bg": "B.A. in English Literature & Elementary Teaching Certification.", "tone": "polite, thorough, thoughtful, and uses emojis like 💡 and 📝"},
    {"id": "T8", "name": "Dr. Anita Desai", "subject": "Class 3 Social Studies & History", "bg": "Ph.D. in History. Dedicated to storytelling in historical education.", "tone": "intellectual, great storyteller, and uses emojis like 🌍 and 🏛️"},
    {"id": "T9", "name": "Mr. Robert Chen", "subject": "Class 3 General Sciences", "bg": "M.S. in Environmental Science. Introduces ecology to young minds.", "tone": "eco-conscious, observant, practical, and uses emojis like 🌿 and ⚡"},
    
    # --- Class 4 Faculty ---
    {"id": "T10", "name": "Prof. Marcus Vance", "subject": "Class 4 Homeroom & Mathematics", "bg": "M.Ed. in Curriculum Design. Passionate about logic systems.", "tone": "highly professional, highly encouraging, and uses emojis like 📊 and 🧠"},
    {"id": "T11", "name": "Miss Chloe Bennett", "subject": "Class 4 Earth & Space Science", "bg": "B.S. in Geology. Coordinates hands-on planetarium modules.", "tone": "adventurous, star-loving, starry-eyed, and uses emojis like 🌌 and 🌎"},
    {"id": "T12", "name": "Mrs. Rebecca Hull", "subject": "Class 4 Creative Writing & Arts", "bg": "B.F.A. in Fine Arts. Focuses on confidence building through theater.", "tone": "theatric, highly expressive, uplifting, and uses emojis like 🎭 and 🌟"},
    
    # --- Class 5 Faculty ---
    {"id": "T13", "name": "Mrs. Elena Rostova", "subject": "Class 5 Homeroom & Social Studies", "bg": "Primary School Educator for over 12 years. Global citizenship advocate.", "tone": "experienced, global-minded, compassionate, and uses emojis like 🗺️ and 🤝"},
    {"id": "T14", "name": "Dr. Alan Turing", "subject": "Class 5 Mathematics & Introductory Coding", "bg": "Ph.D. in Mathematical Logic. Pioneer in digital literacy for schools.", "tone": "analytical, forward-thinking, concise, and uses emojis like 💻 and 🔢"},
    {"id": "T15", "name": "Mr. Samuel Jackson", "subject": "Class 5 Advanced Reading & Literature", "bg": "M.A. in English Prose. Specializes in analytical reading prep.", "tone": "charismatic, articulate, profound, and uses emojis like 🗂️ and 🗣️"}
]

# ==========================================
# 3. COMPLETE PRIMARY STUDENT DATABASE (90 Students)
# ==========================================
STUDENTS_DATABASE = {
    "Class 1": {
        "Liam Smith": {"attendance": "96%", "math": "A", "science": "A-", "english": "B+", "art": "A+"},
        "Noah Johnson": {"attendance": "94%", "math": "B", "science": "A", "english": "A", "art": "A"},
        "Oliver Williams": {"attendance": "98%", "math": "A+", "science": "A+", "english": "A+", "art": "B+"},
        "Elijah Brown": {"attendance": "91%", "math": "C+", "science": "B", "english": "B-", "art": "A"},
        "James Jones": {"attendance": "95%", "math": "A-", "science": "A", "english": "A-", "art": "A-"},
        "William Garcia": {"attendance": "89%", "math": "B-", "science": "C+", "english": "B", "art": "B"},
        "Benjamin Miller": {"attendance": "97%", "math": "A", "science": "A", "english": "A+", "art": "A+"},
        "Lucas Davis": {"attendance": "93%", "math": "B+", "science": "B+", "english": "A-", "art": "A"},
        "Henry Rodriguez": {"attendance": "100%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Alexander Martinez": {"attendance": "95%", "math": "A", "science": "A-", "english": "A", "art": "B+"},
        "Mia Hernandez": {"attendance": "92%", "math": "B", "science": "B", "english": "B+", "art": "A-"},
        "Ava Lopez": {"attendance": "96%", "math": "A-", "science": "A", "english": "A", "art": "A"},
        "Emma Gonzalez": {"attendance": "94%", "math": "B+", "science": "B-", "english": "B", "art": "B+"},
        "Charlotte Wilson": {"attendance": "99%", "math": "A+", "science": "A+", "english": "A", "art": "A+"},
        "Amelia Anderson": {"attendance": "95%", "math": "A", "science": "B+", "english": "A-", "art": "A"},
        "Sophia Thomas": {"attendance": "90%", "math": "C+", "science": "B-", "english": "C+", "art": "A-"},
        "Isabella Taylor": {"attendance": "97%", "math": "A-", "science": "A-", "english": "A", "art": "A"},
        "Evelyn Moore": {"attendance": "96%", "math": "B", "science": "A-", "english": "A-", "art": "B+"}
    },
    "Class 2": {
        "Mason Jackson": {"attendance": "95%", "math": "A", "science": "A", "english": "B+", "art": "A"},
        "Michael Martin": {"attendance": "93%", "math": "B+", "science": "B", "english": "A-", "art": "B+"},
        "Ethan Lee": {"attendance": "97%", "math": "A", "science": "A+", "english": "A", "art": "A+"},
        "Daniel Perez": {"attendance": "88%", "math": "C", "science": "C+", "english": "B-", "art": "A-"},
        "Jacob Thompson": {"attendance": "96%", "math": "A-", "science": "A-", "english": "A", "art": "A"},
        "Logan White": {"attendance": "94%", "math": "B", "science": "B+", "english": "B", "art": "B"},
        "Jackson Harris": {"attendance": "99%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Levi Sanchez": {"attendance": "92%", "math": "B-", "science": "B", "english": "B+", "art": "A-"},
        "Sebastian Clark": {"attendance": "95%", "math": "A", "science": "A", "english": "A-", "art": "B+"},
        "Jack Ramirez": {"attendance": "91%", "math": "B", "science": "B-", "english": "C+", "art": "B"},
        "Harper Lewis": {"attendance": "96%", "math": "A-", "science": "B+", "english": "A", "art": "A"},
        "Ella Robinson": {"attendance": "98%", "math": "A", "science": "A+", "english": "A+", "art": "A+"},
        "Gracie Walker": {"attendance": "93%", "math": "B+", "science": "B", "english": "B", "art": "B+"},
        "Lily Young": {"attendance": "97%", "math": "A", "science": "A-", "english": "A", "art": "A-"},
        "Aria Allen": {"attendance": "94%", "math": "B", "science": "B+", "english": "A-", "art": "A"},
        "Evelyn King": {"attendance": "89%", "math": "C+", "science": "C", "english": "B-", "art": "B"},
        "Avery Wright": {"attendance": "95%", "math": "A-", "science": "A-", "english": "A-", "art": "A"},
        "Scarlett Scott": {"attendance": "96%", "math": "B+", "science": "A", "english": "A", "art": "B+"}
    },
    "Class 3": {
        "Owen Torres": {"attendance": "97%", "math": "A+", "science": "A", "english": "A", "art": "A+"},
        "Theodore Nguyen": {"attendance": "94%", "math": "A-", "science": "B+", "english": "B+", "art": "A"},
        "Samuel Hill": {"attendance": "95%", "math": "B+", "science": "A-", "english": "A-", "art": "B+"},
        "Joseph Flores": {"attendance": "90%", "math": "B-", "science": "B", "english": "C+", "art": "B"},
        "David Green": {"attendance": "98%", "math": "A", "science": "A+", "english": "A+", "art": "A+"},
        "Carter Adams": {"attendance": "92%", "math": "B", "science": "B-", "english": "B", "art": "A-"},
        "Wyatt Nelson": {"attendance": "96%", "math": "A", "science": "A", "english": "A-", "art": "A"},
        "Jayden Baker": {"attendance": "87%", "math": "C", "science": "C+", "english": "C", "art": "B-"},
        "John Hall": {"attendance": "94%", "math": "B+", "science": "B+", "english": "B+", "art": "B"},
        "Asher Rivera": {"attendance": "99%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Chloe Campbell": {"attendance": "95%", "math": "A-", "science": "A-", "english": "A", "art": "A"},
        "Elena Mitchell": {"attendance": "96%", "math": "A", "science": "B+", "english": "A-", "art": "B+"},
        "Maya Carter": {"attendance": "93%", "math": "B", "science": "B", "english": "B", "art": "A-"},
        "Isla Roberts": {"attendance": "100%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Nina Gomez": {"attendance": "91%", "math": "B-", "science": "C+", "english": "B-", "art": "B"},
        "Luna Phillips": {"attendance": "97%", "math": "A", "science": "A", "english": "A", "art": "A-"},
        "Zoe Evans": {"attendance": "94%", "math": "B+", "science": "B+", "english": "A-", "art": "B+"},
        "Vera Turner": {"attendance": "95%", "math": "A-", "science": "A-", "english": "B+", "art": "A"}
    },
    "Class 4": {
        "Leo Diaz": {"attendance": "94%", "math": "B+", "science": "B+", "english": "A-", "art": "B+"},
        "Thomas Cruz": {"attendance": "96%", "math": "A", "science": "A-", "english": "A", "art": "A"},
        "Hudson Ortiz": {"attendance": "98%", "math": "A+", "science": "A+", "english": "A+", "art": "B+"},
        "Gabriel Mendoza": {"attendance": "89%", "math": "C+", "science": "B-", "english": "C+", "art": "B"},
        "Ezra Silva": {"attendance": "95%", "math": "A-", "science": "A", "english": "A-", "art": "A-"},
        "Lincoln Reyes": {"attendance": "92%", "math": "B", "science": "B", "english": "B", "art": "B+"},
        "Isaac Gutierrez": {"attendance": "97%", "math": "A", "science": "A", "english": "A+", "art": "A+"},
        "Ryan Foster": {"attendance": "93%", "math": "B-", "science": "B+", "english": "B+", "art": "A-"},
        "Nathan Garcia": {"attendance": "99%", "math": "A+", "science": "A+", "english": "A", "art": "A+"},
        "Caleb Peterson": {"attendance": "91%", "math": "C", "science": "C+", "english": "B-", "art": "B-"},
        "Ruby Gray": {"attendance": "95%", "math": "A-", "science": "B+", "english": "A-", "art": "A"},
        "Eva Reed": {"attendance": "96%", "math": "A", "science": "A", "english": "A", "art": "A"},
        "Alice Watson": {"attendance": "94%", "math": "B+", "science": "B", "english": "B", "art": "B+"},
        "Ivy Brooks": {"attendance": "100%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Sadie Kelly": {"attendance": "93%", "math": "B", "science": "B-", "english": "B+", "art": "A-"},
        "Iris Sanders": {"attendance": "97%", "math": "A", "science": "A-", "english": "A", "art": "A-"},
        "Piper Price": {"attendance": "95%", "math": "B+", "science": "A-", "english": "A-", "art": "B+"},
        "Lydia Bennett": {"attendance": "96%", "math": "A-", "science": "A", "english": "B+", "art": "A"}
    },
    "Class 5": {
        "Mukesh Kumar": {"attendance": "100%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Colton Barnes": {"attendance": "93%", "math": "B", "science": "B+", "english": "B", "art": "B+"},
        "Cameron Ross": {"attendance": "98%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Carson Henderson": {"attendance": "91%", "math": "B-", "science": "B-", "english": "C+", "art": "B"},
        "Miles Coleman": {"attendance": "95%", "math": "A-", "science": "A", "english": "A-", "art": "A"},
        "Bryson Jenkins": {"attendance": "88%", "math": "C+", "science": "C+", "english": "B-", "art": "B-"},
        "Maverick Perry": {"attendance": "97%", "math": "A", "science": "A", "english": "A", "art": "B+"},
        "Dominic Powell": {"attendance": "94%", "math": "B+", "science": "B", "english": "A-", "art": "A-"},
        "Greyson Long": {"attendance": "99%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Jaxon Patterson": {"attendance": "92%", "math": "B-", "science": "B", "english": "B", "art": "B"},
        "Audrey Hughes": {"attendance": "96%", "math": "A", "science": "A", "english": "A-", "art": "A"},
        "Clara Flores": {"attendance": "95%", "math": "A-", "science": "B+", "english": "A", "art": "A-"},
        "Willow Washington": {"attendance": "94%", "math": "B+", "science": "B-", "english": "B+", "art": "B+"},
        "Stella Butler": {"attendance": "100%", "math": "A+", "science": "A+", "english": "A+", "art": "A+"},
        "Nova Simmons": {"attendance": "93%", "math": "B", "science": "B+", "english": "B", "art": "A"},
        "Lucy Foster": {"attendance": "97%", "math": "A", "science": "A-", "english": "A", "art": "A"},
        "Lily Gonzales": {"attendance": "90%", "math": "C+", "science": "C", "english": "C+", "art": "B"},
        "Emilia Bryant": {"attendance": "96%", "math": "A-", "science": "A-", "english": "A-", "art": "B+"}
    }
}

if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_chat_history" not in st.session_state:
    st.session_state.ai_chat_history = []

# ==========================================
# 4. SECURITY & ACCESS CONTROL
# ==========================================
MASTER_PIN = "23105"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login_user(pin):
    if pin == MASTER_PIN:
        st.session_state.authenticated = True
        st.success("Access Granted!")
        st.rerun()
    elif pin != "":
        st.error("Incorrect Verification PIN. Access Denied.")

def logout_user():
    st.session_state.authenticated = False
    st.rerun()

# --- Secure Login Screen Gate ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏫 EduConnect Primary Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Welcome to the Parent-Teacher Bridge. Please authenticate to continue.</p>", unsafe_allow_html=True)
    
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.info("💡 Portfolio Note: Enter the Master Verification PIN `23105` to access the application dashboard.")
        input_pin = st.text_input("Enter Master Verification PIN:", type="password", help="Required for secure access control.")
        if st.button("Secure Login", use_container_width=True):
            login_user(input_pin)
    st.stop()

# ==========================================
# 5. CONTEXTUAL AI REPLY SIMULATOR ENGINE
# ==========================================
def simulate_teacher_ai_reply(teacher_obj, student_name, student_class, parent_message):
    """Generates context-aware, highly realistic responses based on real database records without API costs."""
    msg = parent_message.lower()
    t_name = teacher_obj["name"]
    t_tone = teacher_obj["tone"]
    
    # Grab the selected student's score parameters dynamically
    scores = STUDENTS_DATABASE[student_class][student_name]
    
    # Context Logic matching keyword arrays
    if "grade" in msg or "marks" in msg or "report" in msg or "result" in msg or "performance" in msg:
        g_math = scores["math"]
        g_sci = scores["science"]
        g_eng = scores["english"]
        
        g_reply_templates = [
            f"Hello! I am happy to discuss performance. Looking closely at our database logs for {student_name}, they currently hold a '{g_math}' grade in Mathematics, a '{g_sci}' in Science, and a '{g_eng}' in English Language. They are staying focused, and I highly recommend keeping up the regular evening review routines at home!",
            f"Thank you for checking in on academic marks! {student_name} is showing consistent application across our branches. Their recorded standing is '{g_math}' in Math and '{g_sci}' in Science. They are adapting wonderfully to the primary curriculum pacing.",
            f"Greetings! Regarding grades, {student_name} has achieved a solid profile: Math is at '{g_math}', Science is at '{g_sci}', and English is at '{g_eng}'. They engage actively during standard instruction blocks."
        ]
        body = random.choice(g_reply_templates)
        
    elif "attendance" in msg or "absent" in msg or "leave" in msg or "late" in msg:
        att = scores["attendance"]
        body = f"Thank you for reaching out. Based on our registration system ledger, {student_name} has a recorded attendance profile of {att} for this active school tier term. Consistency is key in elementary learning blocks, so thank you for ensuring they arrive on schedule!"
        
    elif "behavior" in msg or "conduct" in msg or "discipline" in msg or "fights" in msg or "friend" in msg:
        b_reply_templates = [
            f"Regarding classroom behavior, {student_name} is showing excellent social intelligence! They cooperate beautifully during group science labs and are highly respectful to peers.",
            f"I appreciate your message. {student_name} displays great emotional maturity during our daily homeroom activities. They are helpful, listen closely to instructions, and follow primary rules nicely.",
            f"In terms of classroom engagement, {student_name} is polite and eager to help clean up during transitions. They are building wonderful friendships here!"
        ]
        body = random.choice(b_reply_templates)
        
    else:
        general_templates = [
            f"Thank you for your message! It is an absolute joy having {student_name} in my class. They bring wonderful energy into our workspace every morning. Let me know if you'd like to arrange an in-person conference loop next week!",
            f"Hello there! I've received your note regarding {student_name}. They are doing well and keeping up nicely with our foundational curriculum tracks. Feel free to follow up if you have specific objectives you'd like to work on.",
            f"Warm greetings. Thank you for staying proactive in your child's educational journey. {student_name} is adjusting perfectly to this term's challenges. I look forward to watching them continue to grow!"
        ]
        body = random.choice(general_templates)
        
    # Append localized signature persona
  # Append localized signature persona
    return f'''**[{t_name} - AI Simulation Response]:** \n\n*"Greetings! As an educator who is {t_tone}, I am delighted to respond.* \n\n{body}\n\n*Best regards,* \n**{t_name}***'''

# ==========================================
# 6. DASHBOARD INTERFACE (POST-LOGIN)
# ==========================================

with st.sidebar:
    st.markdown("## 👤 User Session")
    st.markdown("**Role:** Authorized Parent / Guardian")
    st.markdown("---")
    
    navigation = st.radio(
        "🧭 Navigation Menu",
        ["Dashboard Overview", "Student Progress Tracker", "Teacher Directory", "AI Parent-Teacher Chatroom"],
        key="main_navigation" 
    )
    
    st.markdown("---")
    if st.button("🔒 Secure Logout", use_container_width=True, type="secondary"):
        logout_user()

# --- NAVIGATION: DASHBOARD OVERVIEW ---
if navigation == "Dashboard Overview":
    st.title("📊 Primary School Overview Dashboard")
    st.markdown("Welcome to the administrative central control hub.")
    
    total_students = sum(len(students) for students in STUDENTS_DATABASE.values())
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric("Total Enrolled (Classes 1-5)", total_students)
    with m_col2:
        st.metric("Active Faculty Members", len(TEACHERS_DATA))
    with m_col3:
        st.metric("Avg Primary Attendance", "95.2%")
    with m_col4:
        st.metric("Security Gateway Status", "Active (🔒)")
        
    st.markdown("---")
    
    st.subheader("📋 Searchable Primary School Directory")
    st.markdown("Locate student records and matching assigned class tiers instantly:")
    
    flat_student_list = []
    for class_name, students in STUDENTS_DATABASE.items():
        for student_name, metrics in students.items():
            flat_student_list.append({
                "Student Name": student_name,
                "Assigned Tier": class_name,
                "Attendance Record": metrics["attendance"]
            })
    df_all_students = pd.DataFrame(flat_student_list)
    
    search_query = st.text_input("🔍 Quick Global Student Search:", placeholder="Type a name to search across all 5 classes...")
    if search_query:
        df_all_students = df_all_students[df_all_students['Student Name'].str.contains(search_query, case=False)]
        
    st.dataframe(df_all_students, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="mission-box">
        <h4 style='margin-top:0; color: #166534;'>🌟 Our Mission: Helping Society Thrive Through Education</h4>
        EduConnect bridges the critical communication gap between parents and educators. 
        By providing real-time data transparency and open communication vectors, we ensure that no child's academic 
        or emotional development falls through the cracks. This tool empowers families to stay proactive, supporting 
        teachers and driving student success community-wide.
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION: STUDENT PROGRESS TRACKER ---
elif navigation == "Student Progress Tracker":
    st.title("📈 Student Progress Tracker")
    st.markdown("Filter performance logs and detailed report cards by choosing a specific Class.")
    
    selected_class = st.selectbox("Select Class Level:", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"])
    class_roster = STUDENTS_DATABASE[selected_class]
    
    st.markdown(f"### 📋 {selected_class} Roster ({len(class_roster)} Students Registered)")
    selected_student = st.selectbox("Choose Student Profile:", list(class_roster.keys()))
    
    student_info = class_roster[selected_student]
    st.markdown("---")
    st.markdown(f"### 🧑‍🎓 Foundational Progress Card: **{selected_student}**")
    
    meta_col1, meta_col2 = st.columns(2)
    meta_col1.markdown(f"**Current Placement Tier:** `{selected_class}`")
    meta_col2.markdown(f"**Attendance Profile:** 📅 {student_info['attendance']}")
    
    st.markdown("#### Foundational Subject Marks Summary")
    g_col1, g_col2, g_col3, g_col4 = st.columns(4)
    g_col1.metric("Mathematics", student_info['math'])
    g_col2.metric("Science", student_info['science'])
    g_col3.metric("English Language", student_info['english'])
    g_col4.metric("Creative Arts", student_info['art'])

# --- NAVIGATION: TEACHER DIRECTORY ---
elif navigation == "Teacher Directory":
    st.title("👩‍🏫 Expanded Faculty Directory")
    st.markdown("Meet the 15 dedicated elementary educators leading our academic branches across all tiers.")
    
    for i in range(0, len(TEACHERS_DATA), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(TEACHERS_DATA):
                teacher = TEACHERS_DATA[i + j]
                with cols[j]:
                    st.markdown(f"### {teacher['name']}")
                    st.info(f"**Role:** {teacher['subject']}")
                    st.write(f"*{teacher['bg']}*")
        st.markdown("---")

# --- NAVIGATION: AI PARENT-TEACHER CHATROOM (NEW FEATURE) ---
elif navigation == "AI Parent-Teacher Chatroom":
    st.title("🤖 AI Parent-Teacher Chat Assistant")
    st.markdown("Select a class, choose your child's profile, and send a live message to any teacher. The AI simulation engine will respond instantly using the teacher's exact professional records.")
    
    cc_col1, cc_col2 = st.columns(2)
    with cc_col1:
        chat_class = st.selectbox("1. Target Class Tier:", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"], key="chat_c")
    with cc_col2:
        chat_student = st.selectbox("2. Child Profile Context:", list(STUDENTS_DATABASE[chat_class].keys()), key="chat_s")
        
    teacher_names = [t["name"] for t in TEACHERS_DATA]
    selected_teacher_name = st.selectbox("3. Address Message To:", teacher_names, key="chat_t")
    
    # Locate full teacher meta dictionary matching the target name configuration
    target_teacher_obj = next(t for t in TEACHERS_DATA if t["name"] == selected_teacher_name)
    
    st.markdown("---")
    st.subheader(f"💬 Live Message Feed with {selected_teacher_name}")
    
    # Render historical layout structures
    for chat_block in st.session_state.ai_chat_history:
        if chat_block["recipient"] == selected_teacher_name and chat_block["student"] == chat_student:
            if chat_block["sender"] == "Parent":
                st.chat_message("user").write(chat_block["text"])
            else:
                st.chat_message("assistant").write(chat_block["text"])
                
    # Chat Input block element
    parent_input = st.chat_input(f"Ask {selected_teacher_name} about {chat_student}'s grades, attendance, or behavior...")
    
    if parent_input:
        # Commit parent message to record logs
        st.session_state.ai_chat_history.append({
            "sender": "Parent", "recipient": selected_teacher_name, "student": chat_student, "text": parent_input
        })
        st.chat_message("user").write(parent_input)
        
        # Trigger clean simulation response execution loop
        with st.spinner(f"{selected_teacher_name} is typing a response..."):
            time.sleep(1)  # Brief simulated latency for realism effect
            ai_reply_text = simulate_teacher_ai_reply(target_teacher_obj, chat_student, chat_class, parent_input)
            
        st.session_state.ai_chat_history.append({
            "sender": "Teacher_AI", "recipient": selected_teacher_name, "student": chat_student, "text": ai_reply_text
        })
        st.chat_message("assistant").write(ai_reply_text)