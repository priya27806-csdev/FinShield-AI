import streamlit as st

st.set_page_config(page_title="FinShield AI")

st.title("FinShield AI")
st.caption("Your digital payment safety assistant")

st.divider()

st.subheader("Check a suspicious message")
st.write("Paste a payment message below to check for warning signs.")

message = st.text_area(
    "Payment Message",
    placeholder="Paste your message here..."
)

if st.button("Check Message", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        text = message.lower()

        high_risk = ["otp", "password", "pin", "urgent", "blocked"]
        medium_risk = ["click here", "claim prize", "send money"]

        found_high = [word for word in high_risk if word in text]
        found_medium = [word for word in medium_risk if word in text]

        if found_high:
            st.error("HIGH RISK")
            st.write("Warning signs:", ", ".join(found_high))

        elif found_medium:
            st.warning("MEDIUM RISK")
            st.write("Warning signs:", ", ".join(found_medium))

        else:
            st.success("LOW RISK")
            st.write("No listed warning signs found.")

        st.info(
            "Safety Tip: Never share your OTP, PIN or password. "
            "Always verify the sender before taking action."
        )

st.divider()
st.caption("FinShield AI | Student Project | Prototype")
