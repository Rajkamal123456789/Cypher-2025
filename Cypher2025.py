import streamlit as st
import hashlib

st.set_page_config(page_icon="hacker.png")

st.markdown("""
<style>
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}
.floating-text {
    animation: float 3s ease-in-out infinite;
    color: #4A90E2;
    font-size: 2.5em;
    text-align: center;
    margin: 20px 0;
}
.result-box {
    border: 2px solid #36363b;
    border-radius: 5px;
    padding: 15px;
    margin: 20px 0;
    background-color: #f23c05;
}
</style>
""", unsafe_allow_html=True)



def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = ord(char) - base
            if mode == 'encrypt':
                shifted = (shifted + shift) % 26
            else:
                shifted = (shifted - shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def process_key(key):
    
    return 12345678


if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'mode' not in st.session_state:
    st.session_state.mode = None


if st.session_state.page == 'home':
    
    st.markdown('<div class="floating-text">🔒 Cypher 2025</div>', unsafe_allow_html=True)
    st.markdown("""
    ## Welcome to Cypher 2025!
    **Your Ultimate Message Security Solution**
    
    Features:
    - Military-grade encryption
    - Instant decryption
    - Secure key-based access
    """)
    
    if st.button("🚀 Launch Encryptor/Decryptor"):
        st.session_state.page = 'app'
        st.rerun()

elif st.session_state.page == 'app':
    
    #st.title("🔐 Cypher 2025")
    st.markdown('<div class="floating-text">🔐 Cypher 2025</div>', unsafe_allow_html=True)

  
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("🔒 Encryption", use_container_width=True):
            st.session_state.mode = 'encrypt'
    with col2:
        if st.button("🔓 Decryption", use_container_width=True):
            st.session_state.mode = 'decrypt'

    
    if st.session_state.mode:
        st.success(f" {st.session_state.mode.upper()} MODE ACTIVATED ".center(50, '✨'))
    else:
        st.warning("Please select a mode above")
    
    
    with st.form("crypto_form"):
        message = st.text_area("Enter your message", height=150)
        key = st.text_input("Enter security key", type="password")
        submitted = st.form_submit_button("🚀 Process Message")
        
        
        
        if submitted:
            
            if not message or not key:
                st.error("Please fill both message and key fields!")
                
            elif key != '1234':
                col1, col2 = st.columns([1,1])
                with col1:
                    st.warning("security key 🔐 invalid!")
                with col2:
                    st.info("security key is '1234'")
                
                
            else:
                shift = process_key(key)
                try:
                    if st.session_state.mode == 'encrypt':
                        processed = caesar_cipher(message,shift, 'encrypt')
                        emoji = "🔒"
                    else:
                        processed = caesar_cipher(message, shift, 'decrypt')
                        emoji = "🔓"
                    
                    st.markdown(f"""
                    <div class="result-box">
                        <center>
                            <h3>{emoji}Result</h3>
                            <pre>{processed}</pre>
                        </center>
                    </div>
                    """,unsafe_allow_html=True)
                    
                    
                except Exception as e:
                    st.error(f"Error processing message: {str(e)}")
            

    
    if st.button("🏠 Return to Home"):
        st.session_state.page = 'home'
        st.rerun()
        
st.html("<center><font color=""gray""><p> &#169; 2025 Rajkamal Ravichandran. All rights reserved.</p></center>")
