import streamlit as st
from sheets_helper import get_contacts
from email_sender import send_email
from content_generator import get_template

st.set_page_config(page_title="Genie - IMA Connect", layout="centered")
st.title("🤖 Genie - Your Influencer Outreach Assistant")

target = st.selectbox("Who are you reaching out to?", ["Brand", "Influencer"])
country = st.text_input("Target Country")
niche = st.text_input("Niche")
num_to_send = st.number_input("Number of emails/DMs to send", min_value=1, step=1)

if target == "Influencer":
    min_followers = st.number_input("Minimum followers", min_value=0, step=1000)
    max_followers = st.number_input("Maximum followers", min_value=0, step=1000)
else:
    min_followers = max_followers = None

if st.button("Send Outreach"):
    contacts = get_contacts(target, country, niche, num_to_send, min_followers, max_followers)
    template = get_template(target)
    for contact in contacts:
        send_email(contact, template, target)
    st.success(f"Sent {len(contacts)} messages successfully!")