import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Streamlit Contact Form
@st.dialog("Contact Me")
def show_contact_form():
    full_name = st.text_input("Full Name")
    phone_number = st.text_input("Enter your Phone Number")
    email = st.text_input("Enter Your Email")
    message = st.text_area("Message")

# Submit button
    if st.button("Submit"):
    # Validate input fields
        if not full_name or not phone_number or not email or not message:
            st.error("All fields are required.")
        else:
        # Send email
            response = send_email(full_name, phone_number, email, message)
            if response == "Success":
             st.success("Success! Your message has been submitted.")
            else:
             st.error(response)

# Layout with two columns
col1, col2 = st.columns(2, gap="large")

with col1:
    # Load and process the image
    image = Image.open("mywebpage/views/johnson.jpeg")
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    # Apply the mask to the image
    circular_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)

    # Display the circular image
    st.image(circular_image, caption="Johnson", use_container_width=True)

with col2:
    st.title("Johnson  Njenga")
    st.write(
        "Founder of J&John Software Company based in Kenya and also a Computer Science student at the University Of the People."
    )
    if st.button("Contact me"):
        show_contact_form()

# Function to send an email
def send_email(full_name, phone_number, email, message):
    try:
        # Your email credentials
        sender_email = ""
        sender_password = ""  # Use an App Password if using Gmail
        receiver_email = ""

        # Create the email
        subject = f"Contact Form Submission from {full_name}"
        body = f"""
        Name: {full_name}
        Phone Number: {phone_number}
        Email: {email}
        Message: {message}
        """

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return "Success"
    except Exception as e:
        return f"Failed to send email: {e}"
    
#Exprience
st.write("\n")
st.subheader("MY EXPIRIENCE & QUALIFICATIONS", anchor=False)

st.write(
    """
        - 2 Years of exprience in software development and IT field.
        - Strong hands-on exprience and knowledge in python and Java.
        - Good understanding of statistical principles and their respective applications.
        - Good leadership and excellent team-player displaying a strong sense of initiative on tasks.
    """
)

# My skills

st.write("\n")
st.subheader("MY SKILLS", anchor=False)

st.write(
    """
        - Programming: Python (Pandas, Tkinter, Streamlit), JAVA, SQL
        - Databases: MongoDB, MySQL
        - Data Visualization: Ms Excel
        - HTML , CSS, Firebase and Git
    """
)
#
# My certifications
st.write("\n")
st.subheader("My CERTIFICATIONS", anchor=False)

st.write(
    """
        - Professional Certificate in Cybersecuriy by Google.
        - Certificate in python by Hackerrank.
        - Certificate in web development by Mindluster.
        - Certificate in Risk management by Oxford Home Study Center.
        - Certificate in Project Management by Oxford Home Study Center.
        - Certificate in Blockchain and Cryptocurrency by Alison.
    """
        )

# Projects
st.write("\n")
st.subheader("MY PROJECTS")

st.markdown(
    """
    [![Library Management system](https://img.shields.io/badge/GitHub-Libtrary-blue?logo=github)](https://github.com/Johnsonndungu/Library-management-system)
    [![Quiz App](https://img.shields.io/badge/GitHub-Quiz_App-blue?logo=github)](https://github.com/Johnsonndungu/Quiz-app-in-Java)
    [![Support Tickets](https://img.shields.io/badge/GitHub-Customer_Ticket_Tool-blue?logo=github)](https://github.com/Johnsonndungu/support-tickets-1)
    [![Car Rental System](https://img.shields.io/badge/GitHub-car_Rental_system-blue?logo=github)](https://github.com/Johnsonndungu/carrentalcomany)
    """,
    unsafe_allow_html=True
)
