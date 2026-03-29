import streamlit as st
import urllib.parse # This helps clean up the text for the AI

st.set_page_config(page_title="Magic Art App", page_icon="🎨")

st.title("My Magic Art Box 🎨")
st.write("Type something fun and watch the AI draw it!")

# 1. Ask the user for an idea
user_prompt = st.text_input("What should the AI draw?", placeholder="A space panda eating pizza")

if st.button("Make Magic! ✨"):
    if user_prompt:
        st.write(f"The artist is now drawing: **{user_prompt}**...")
        
        # 2. Prepare the prompt for the AI (cleaning up spaces)
        encoded_prompt = urllib.parse.quote(user_prompt)
        
        # 3. This is the Magic Link to the AI Artist
        # We add 'seed' to make sure every image is unique!
        import random
        seed = random.randint(0, 99999)
        image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={seed}"
        
        # 4. Show the masterpiece!
        st.image(image_url, caption=f"Your {user_prompt}", use_container_width=True)
        
        st.success("Ta-da! Your art is ready!")
    else:
        st.warning("Please type something first so the artist knows what to draw!")

st.divider()
st.caption("Built with 💖 and a little bit of Magic.")