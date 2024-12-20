import streamlit as st

st.title("Still in development")
import streamlit.components.v1 as components

# Embedding the chatbot using an HTML snippet
chatbot_html = """
<!DOCTYPE html>
<html>
<head>
    <!-- Embed Chatbot Script -->
    <script async type='module' src='https://interfaces.zapier.com/assets/web-components/zapier-interfaces/zapier-interfaces.esm.js'></script>
<zapier-interfaces-chatbot-embed is-popup='false' chatbot-id='cm4wut83s00091423o4daisoa' height='600px' width='400px'></zapier-interfaces-chatbot-embed>
</head>
<body>
    </script>
</body>
</html>
"""

# Display chatbot in Streamlit
components.html(chatbot_html, height=600, scrolling=True)
